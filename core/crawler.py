# -*- coding: utf-8 -*-
try:
    from src.Colors import TextColor
    from src.libs import sleep
    import src.libs as lib
    from src.libs import Thread
    import os
except Exception as err:
    raise SystemExit, TextColor.RED + str('Something is wrong when we want to import libraries: %s'%(err)) + TextColor.WHITE

define_headers = { #set http header for our requests you can add anothers http headers to this dictionary
    "user-agent":
        "Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25"
}

''' Function
    name: SetWebSiteUrl
    parameters: url of site --> example: http://example.com
    return: That web site is available or not -> then pass it to the next function for crawling 
'''
def SetWebSiteUrl(url): #set url of rhost for crawling
    if not url.startswith('http://') and not url.startswith('https://'):
        print TextColor.RED + str('\n[-]Please enter url correctly\n') + TextColor.WHITE
    else:
        try:
            print TextColor.WARNING + str('[*] Please wait to get response from %s ...'%(url)) + TextColor.WHITE

            if url.startswith('http://'): #send request.get for read content of web page
                response = lib.requests.get(url, headers=define_headers, allow_redirects=False).status_code
            else:
                response = lib.requests.get(url, headers=define_headers, verify=False, allow_redirects=False).status_code

            if response == 200: #if response is ok and web page is on so we can start the crawling
                print TextColor.GREEN + str('[+] Remote host has been set ...') + TextColor.WHITE
                sleep(0.5)
                print TextColor.WARNING + str('[+] Start crawl ... \n') + TextColor.WHITE
                num = raw_input(TextColor.PURPLE + TextColor.BOLD + str('Enter depth of crawl / [Enter !! for auto crawling]: ') \
                                + TextColor.WHITE)
                GetAllLinks(url, num)
            else: #else user must check that what happened that we can send request to web page
                print TextColor.RED + str('[-] Fail to set rhost :(') + TextColor.WHITE

        except Exception as err:
            print TextColor.RED + str('[-] Some error with socket-> %s \n'%(err)) + TextColor.WHITE
#--------------------------------------------------
''' Function
    name: GetAllLinks
    parameter: url of site -> example: http://example.com
    return: get all link in source code of web page
'''
def GetAllLinks(url, num):
    Crawler(url, num) # Crawler class code is below
#--------------------------------------------------
""" Class
    name: Crawler
    parameter:|root  => get base url of web site
              |depth => how many layer do want to go?
    private methods =>{
        1.__GetLinks__
        2.__init__
    }
"""
class Crawler(object):
    def __init__(self, root, depth):
        self.root = root
        self.host = lib.urlparse.urlparse(root)[1]      #Get host name from url
        self.protocol = lib.urlparse.urlparse(root)[0]  #Get host protocol from url
        self.depth = depth                              #number of crawl in website
        self.urls_seen = set()                          #Used to avoid putting duplicate links in queue

        self.__GetLinks__()

    def __GetLinks__(self):
        url_queue = lib.Queue()
        url_queue.put(self.root)

        print TextColor.RED + str('################# Start Crawling #################') + TextColor.WHITE

        counter_depth = 0

        while not url_queue.empty():

            current_url = url_queue.get()
            self.urls_seen.add(current_url)

            if self.depth != "!!":
                if counter_depth == int(self.depth):
                    print
                    print TextColor.WARNING + str(" ------- Done ------- ") + TextColor.WHITE
                    print
                    break

            counter_depth = counter_depth + 1

            try:
                if self.protocol is 'http':
                    response = lib.requests.get(current_url, headers=define_headers, allow_redirects=False)
                else:
                    response = lib.requests.get(current_url, headers=define_headers, allow_redirects=False, verify=False)

                #algorithm of crawling on website page
                if response.status_code == 200:

                    soup = lib.BS(response.content)#, "lxml")
                    # soup = lib.BS(response.content, "lxml") todo = this line dose not work for mac os
                    for line in soup.find_all('a', href=True):
                        if lib.urlparse.urlparse(line['href']):
                            sleep(0.2)
                            if line['href'].startswith('http') or line['href'].startswith('https'):
                                if line['href'].startswith(self.root):
                                    if line['href'] not in self.urls_seen:
                                        print TextColor.BLUE + str('[%d, %s] => '%(counter_depth, current_url) \
                                                                   + line['href']) + TextColor.WHITE
                                        url_queue.put(line['href'])
                                        _thr_ = Thread.Thread(target=self.WriteUrlsInFile, args=(line['href'],))
                                        _thr_.daemon = True
                                        _thr_.start()
                                    else: continue
                            else:
                                if line['href'].startswith('/'):
                                    if self.root + line['href'] not in self.urls_seen:
                                        print TextColor.BLUE + str('[%d, %s] => '%(counter_depth, current_url) \
                                                                   + self.root + line['href']) + TextColor.WHITE
                                        self.ThreadPool(self.root + line['href'])
                                        url_queue.put(self.root + line['href'])

                                    else: continue
                                elif not line['href'].startswith('/') or not \
                                        line['href'].startwith('http') or not line['href'].startswith('https'):
                                    if (self.root + '/' + line['href']) not in self.urls_seen:
                                        print TextColor.BLUE + str('[%d, %s] => '%(counter_depth, current_url) + \
                                                                   self.root + '/' + line['href']) + TextColor.WHITE
                                        self.ThreadPool(self.root + '/' + line['href'])
                                        url_queue.put(self.root + '/' + line['href'])

                                    else: continue
                                else:
                                    if line['href'] not in self.urls_seen:
                                        print TextColor.BLUE + str('[%d, %s] =>'%(counter_depth, current_url) + \
                                                                   line['href']) + TextColor.WHITE
                                        self.ThreadPool(line['href'])
                                        url_queue.put(line['href'])
                                    else: continue

                else:
                    print
                    print TextColor.RED + str('[code: %d] => %s'%(response.status_code, current_url)) + TextColor.WHITE
                    print

            except Exception:
                continue
        url_queue.task_done()

    def ThreadPool(self, url):
        _thr_ = Thread.Thread(target=self.WriteUrlsInFile,
                              args=(url,))
        _thr_.daemon = True
        _thr_.start()

    """
        function: WriteUrlsInFile
        mode: private
        return: write url in file
        parameter: url => get url that we must write in file
    """
    def WriteUrlsInFile(self, url):
        all_url_wrote = set()

        if not os.path.exists('crawledlink'):
            os.mkdir('./crawledlink')

        if not os.path.exists('./crawledlink/' + self.host): #check that destination file is exist or  not
            open('./crawledlink/' + self.host, 'a')#if not we create that file

        with open('./crawledlink/' + self.host, 'r') as file:
            for item in file.readlines():
                all_url_wrote.add(item)

        if url not in all_url_wrote:
            with open('crawledlink/' + self.host, 'a') as file:
                file.write(url + "\n")
        else: pass
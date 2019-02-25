import re

import requests as reqs



response = reqs.get("https://google.com/search?q={query}&btnG=Search&hl=en-US&biw=&bih=&gbv=1&start={page_no}&filter=0".format(query="index.php?id=", page_no=1),
                    params=None)


def extract_domains(resp):

    link_regx = re.compile('<cite.*?>(.*?)</cite>')
    try:
        links_list = link_regx.findall(resp)

        for link in links_list:
            print (link.replace("<b>", '')).replace("</b>", "")
    except Exception:
        pass

extract_domains(response.content)

'''
    Use this sites for website recon
    
  for more detail of recon ==> https://toolbar.netcraft.com/site_report?url=https://aranuma.com
  for subdomain  ==> https://searchdns.netcraft.com/?restriction=subdomain+matches&host=downloadme.ir&lookup=wait..&position=limited
    
'''



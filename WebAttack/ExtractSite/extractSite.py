try:
    from src.Colors import TextColor
    import src.libs as lib
    from Config.WebConfig import define_headerdata
    import os
except Exception as error:
    raise SystemExit, "\033[31m" + "%s" % error + "\033[0m"

extractPath = ""


def Mask():
    print 'Extract site'


def StartExtractSite():

    print 'Please wait comming soon'
    return

    global extractPath

    if not os.path.exists('./outputs/ExtractedSite'):
        os.mkdir('./outputs/ExtractedSite')

    url = raw_input(TextColor.CVIOLET + '~ FHack/# Enter url of site: ' + TextColor.WHITE)

    print TextColor.WHITESMOKE + '[*] Please wait to set rhost' + TextColor.WHITE

    define_headerdata['referer'] = url

    response = lib.requests.get(url=url, params=None, headers=define_headerdata, verify=False)

    lib.sleep(1)

    if response.status_code == 200:
        print TextColor.GREEN + "[+] Rhost is set successfully" + TextColor.WHITE
        depth = raw_input(TextColor.CVIOLET + "~ FHack/# Enter depth of extraction: " + TextColor.WHITE)

        if not os.path.exists('./outputs/ExtractedSite/' + url):
            os.mkdir('./outputs/ExtractedSite/' + url)
            extractPath = str('./outputs/ExtractedSite/' + url)

        print TextColor.GREEN + "[+] Depth set: %d" % int(depth) + TextColor.WHITE
        print TextColor.WARNING + "[++] Output of site location: " + os.getcwd() + "/outputs/" + TextColor.WHITE

    else:
        print TextColor.RED + '[-] Rhost is not available please check that you enter it correct or not' \
              + TextColor.WHITE


if __name__ == "__main__":
    try:
        StartExtractSite()
    except Exception as error:
        raise SystemExit, TextColor.RED + "some exception as : %s" % error + TextColor.WHITE

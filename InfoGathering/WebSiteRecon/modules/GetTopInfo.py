try:
    from src.Colors import TextColor
    import src.libs as lib
    from Config.WebConfig import define_headerdata

except Exception as error:
    raise SystemExit, '\033[31m' + 'Something wrong in GetTopInfo[WebSiteRecon] package' + '\033[0m'


def GetTopInfs():

    #https://toolbar.netcraft.com/site_report?url=https://aranuma.com

    rhost = raw_input(TextColor.CVIOLET + '==> Enter website url: ')

    response = lib.requests.get('https://toolbar.netcraft.com/site_report',
                                params={"url":"https://aranuma.com"}, verify=False,
                                headers=define_headerdata

                                )

    print response.content

    pass

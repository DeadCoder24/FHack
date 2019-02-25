try:
    from src.Colors import TextColor
    import src.libs as lib
    from socket import gethostbyname
    from Config.WebConfig import API_KEY_ip_geolocation
    import json
except Exception as error:
    raise SystemExit, '\033[31m' + 'Something wrong in GetTopInfo[WebSiteRecon] package' + '\033[0m'


def GetGeoInfs():

    rhost = raw_input(TextColor.CVIOLET + '==> Enter website url as (example.com) or ip: ')

    session = lib.requests.Session()

    response = session.get("http://ip-to-geolocation.com/api/json/{ip}?key={apikey}".
                   format(ip=gethostbyname(rhost), apikey=API_KEY_ip_geolocation))

    with session:
        jsonRes = json.loads(str(response.content))

        listColumns = list()
        for key in jsonRes.keys():
            listColumns.append(str(key))

        counter = 0
        make_table = lib.mytable(['info', 'item'])
        for item in jsonRes.keys():
            make_table.add_row([item, jsonRes[item]])
            counter += 1

        print TextColor.CYELLOW + str(make_table) + TextColor.WHITE

    # todo = log result to ouputs files
try:
    from src.Colors import TextColor
    import src.libs as libs
    from .ReconMask import MainMask
    from .modules.GetTopInfo import GetTopInfs
except Exception as error:
    raise SystemExit, "\033[31m" + "Something wrong in importing the library in WebsiteReconMainHandler" + "\033[0m"


def SubMenu():
    MainMask()

    print

    print TextColor.CVIOLET + '\t\t==> [1]. Get top info'
    print '\t\t==> [2]. Get emails'


def WebSiteReconMain():
    SubMenu()

    print

    selectedSubMenuItem = raw_input(TextColor.CVIOLET + '~fhack/InfoGathering/[WebRecon]#' + TextColor.WHITE)

    if selectedSubMenuItem == '1':
        GetTopInfs()
    elif selectedSubMenuItem == '2':
        pass
    elif selectedSubMenuItem == '0':
        print
        return

try:
    from src.Colors import TextColor
    import src.libs as libs
    from .ReconMask import MainMask
except Exception as error:
    raise SystemExit, "\033[31m" + "Something wrong in importing the library in WebsiteReconMainHandler" + "\033[0m"


def SubMenu():
    MainMask()

    print

    print TextColor.CVIOLET + '\t\t==> [1]. Get top info'
    print '\t\t==> [2]. Get emails'
    print '\t\t==> [3]. Get ' + TextColor.WHITE


def WebSiteReconMain():
    SubMenu()

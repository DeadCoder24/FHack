try:
    from Config import RecOS
    from src.Colors import TextColor
    import os
except Exception as error:
    raise SystemExit, '\033[31m' + "%s" % error + "\033[0m"


def LinuxDebian_Ubuntu_Setup():

    def InstallCreateMalwareTools():
        os.system("sudo apt-get install apktool")

    InstallCreateMalwareTools()

def main():

    os.system("sudo pip install -r libs_used")

    if RecOS.IsOSLinux():
        if "Ubuntu" in RecOS.getLinuxDistr():
            LinuxDebian_Ubuntu_Setup()


if __name__ == "__main__":
    main()


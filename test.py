def main():
    print
    CreateIp(raw_input('Enter ip range (192.168.1.1-192.168.2.200): '))


def CreateIp(ip):
    # "192.255.254.254-193.0.1.1

    IP_startFrom = (ip.split('-')[0]).split('.')
    IP_endBy = (ip.split('-')[1]).split('.')

    ip1 = ''.join(IP_startFrom)
    ip2 = ''.join(IP_endBy)

    if ip1 > ip2:
        return

    if IP_startFrom[0] < IP_endBy[0]:  # Type A

        x1 = int(IP_startFrom[0])
        x2 = int(IP_startFrom[1])
        x3 = int(IP_startFrom[2])
        x4 = int(IP_startFrom[3])

        while x4 < 255:

            newIp = str(x1) + '.' + str(x2) + '.' + str(x3) + '.' + str(x4)
            print newIp

            if x4 == 254:
                x3 = x3 + 1
                x4 = 0

            if x3 == 256:
                x2 = x2 + 1
                x3 = 0
                x4 = 0

            if x2 == 256:
                x1 = x1 + 1
                x2 = 0
                x3 = 0
                x4 = 0

            if (newIp.split('.')[0] == IP_endBy[0]
                    and newIp.split('.')[1] == IP_endBy[1]
                    and newIp.split('.')[2] == IP_endBy[2]
                    and newIp.split('.')[3] == IP_endBy[3]):
                break

            x4 = x4 + 1


    elif IP_startFrom[1] < IP_endBy[1]:  # Type B => x.m.x.x-x.n.x.x    n > m

        x2 = int(IP_startFrom[1])
        x3 = int(IP_startFrom[2])
        x4 = int(IP_startFrom[3])

        while x4 < 255:

            newIp = IP_startFrom[0] + '.' + str(x2) + '.' + str(x3) + '.' + str(x4)
            print newIp

            if x4 == 254:
                x3 = x3 + 1
                x4 = 0

            if x3 == 256:
                x2 = x2 + 1
                x3 = 0
                x4 = 0

            if (newIp.split('.')[1] == IP_endBy[1]
                    and newIp.split('.')[2] == IP_endBy[2]
                    and newIp.split('.')[3] == IP_endBy[3]):
                break

            x4 = x4 + 1

    elif IP_startFrom[2] < IP_endBy[2]:  # Type C => x.x.m.x-x.x.n.x    n > m

        x4 = int(IP_startFrom[3])
        x3 = int(IP_startFrom[2])

        while x4 < 255:
            newIp = IP_startFrom[0] + '.' + IP_startFrom[1] + '.' + str(x3) + '.' + str(x4)
            print newIp

            if x4 == 254:
                x3 = x3 + 1
                x4 = 0

            if newIp.split('.')[2] == IP_endBy[2] and newIp.split('.')[3] == IP_endBy[3]:
                break

            x4 = x4 + 1

    elif IP_startFrom[3] < IP_endBy[3]:  # Type D => x.x.x.m-x.x.x.n    n > m
        for i in xrange(2, int(IP_endBy[3]) + 1):
            if int(IP_startFrom[3]) < int(IP_endBy[3]):
                createdIp = IP_startFrom[0] + '.' + IP_startFrom[1] + '.' + IP_startFrom[2] + '.' + str(i)
                print createdIp

    return


if __name__ == "__main__":
    main()

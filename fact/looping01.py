#!/usr/bin/env python3

"""
For - a simple for loop
"""


def main():
    # for-loop is perfect for stepping through this list
    iplist = ["10.1.1.1", "10.2.2.2", "10.3.3.3"] # list of IP (str)

    # 'ip' is just a variable as we step through iplist
    for ip in iplist:
        print(ip)

    # open file in read mode
    dnsfile = open("dnsservers.txt", "r")
    # create list of lines
    dnslist = dnsfile.readlines()

    # loop over lines
    for svr in dnslist:
        # print and end without newline
        print(svr, end="")

    # close the file
    dnsfile.close()  # best practice to close file

    with open("dnsservers.txt", "r") as dnsfile2:
        # incident to keep the dnsfile object open
        # create list of lines
        dnslist2 = dnsfile2.readlines()
        # loop over lines
        for svr in dnslist2:
            # print and end without newline
            print(svr, end="")


if __name__ == "__main__":
    main()

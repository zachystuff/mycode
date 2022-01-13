#!/usr/bin/python3

loginfail = 0

with open('logs.txt') as logfile:
    for line in logfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1  # this is the same as loginfail = loginfail + 1

print("The number of failed log in attempts is", loginfail)

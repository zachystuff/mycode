#!/usr/bin/env python3

def main():

    grade = input("What is the students current grades?")
    message = "The student's grade is an "

    if int(grade) < 60:
        message = message + "F"
    elif int(grade) < 70:
        message = message + "D"
    elif int(grade) < 80:
        message = message + "C"
    elif int(grade) < 90:
        message = message + "B"
    elif int(grade) <= 100:
        message = message + "A"
    else:
        message = "Enter a valid number"

    print(message)
    print("Exiting the script")


main()

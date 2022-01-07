#!/usr/bin/python


def maxnum(num1: int, num2: int, num3: int) -> int:
    """
    write a function that returns the max of 3 numbers
    :return: number
    """
    maxinput = 0
    if num1 > maxinput:
        maxinput = num1
    if num2 > maxinput:
        maxinput = num2
    if num3 > maxinput:
        maxinput = num3

    return maxinput


def main():
    print(maxnum(1, 2, 3))  # expected 3

    print(maxnum(6, 4, 1))  # expected 6

    print(maxnum(1, 9, 6))  # expected 9


if __name__ == "__main__":
    main()


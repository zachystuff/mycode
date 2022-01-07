#!/usr/bin/env python3


def reversestring(string: str) -> str:
    """
    Write a Python function to multiply all the numbers in a list.
    :param string: list[int]
    :return: int
    """
    return string[::-1]


def main():
    print(reversestring("zach"))
    print(reversestring("Yusuf"))


if __name__ == "__main__":
    main()

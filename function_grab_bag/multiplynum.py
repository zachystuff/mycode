#!/usr/bin/env python3


def multiplynum(numlist: list[int]) -> int:
    """
    Write a Python function to multiply all the numbers in a list.
    :param numlist: list[int]
    :return: int
    """
    product = 1
    for num in numlist:
        product *= num

    return product


def main():
    print(multiplynum([2, 3, 4, 5]))
    print(multiplynum([7, 8, 9, 10]))


if __name__ == "__main__":
    main()

#!/usr/bin/python3

def sumnum(nums: list[int]) -> int:
    """
    Function that takes in and number and returns a sum of numbers
    :param nums: list[int]
    :return: int
    """
    sumnums = 0
    for num in nums:
        sumnums += num
    return sumnums


def main():
    print(sumnum([1, 2, 3, 4, 5]))  # 15
    print(sumnum([2, 3, 4]))  # 9
    print(sumnum(["a", "b", 1, 2, 3]))  # expecting error to be thrown


if __name__ == "__main__":
    main()

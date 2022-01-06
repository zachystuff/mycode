#!/usr/bin/env python3

def main():
    for i in range(4):
        print(i)

    for x in range(5):
        print(x, end=" ")

    fruitbowl: list[str] = ["apple", "pear", "grapes"]
    for fruit in fruitbowl:
        print("\n", fruit)

    foo = open("ourfile.txt", "w")
    for fruit in fruitbowl:
        print(fruit, file=foo)
    foo.close()


if __name__ == "__main__":
    main()

#!/usr/bin/python3

"""
Learning about for loops in python
"""


def main():
    # create the list of vendors
    vendors = ["cisco", "juniper", "big_ip", "f5", "arista"]
    approved_vendors = ["cisco", "juniper"]
    # loop across the vendors
    for vendor in vendors:
        print(f"the vendor is: {vendor}")

        # take note of the not in. Very useful
        if vendor not in approved_vendors:
            print(" - NOT AN APPROVED VENDOR! ")

    print("\nOur loop has ended")


if __name__ == "__main__":
    main()


import sys

#!/usr/bin/env python3
"""
print_flat_star.py

Print a simple centered star pyramid.

Usage:
    python print_flat_star.py [height]

If height is not provided, you'll be prompted for it.
"""



def print_pyramid(height: int, char: str = '*') -> None:
    """Print a centered pyramid of given height using char."""
    if height <= 0:
        return
    for i in range(1, height + 1):
        spaces = height - i
        stars = 2 * i - 1
        print(' ' * spaces + char * stars)


def main():
    height = None
    if len(sys.argv) > 1:
        try:
            height = int(sys.argv[1])
        except ValueError:
            pass

    while height is None:
        try:
            height = int(input("Enter pyramid height (positive integer): ").strip())
        except (ValueError, EOFError):
            print("Please enter a valid positive integer.")
            height = None

    print_pyramid(max(0, height))


if __name__ == "__main__":
    main()
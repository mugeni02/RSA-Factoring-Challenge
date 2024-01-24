#!/usr/bin/env python3

import sys

def factorize(number):
    """Factorize a number into two smaller numbers.

    Args:
        number (int): The number to factorize.

    Returns:
        tuple: A tuple containing the factorization (p, q).
    """
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return (i, number // i)
    return None

def main(filename):
    """Read numbers from a file and output their factorization."""
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                factors = factorize(number)
                if factors:
                    print(f"{number}={factors[0]}*{factors[1]}")
                else:
                    print(f"{number} is a prime number")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid number in the file.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)


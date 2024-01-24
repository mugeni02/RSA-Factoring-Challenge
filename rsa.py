#!/usr/bin/env python3

import sys

def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def factorize_rsa_number(n):
    """Factorize an RSA number into prime numbers p and q."""
    for p in range(2, n):
        if is_prime(p) and n % p == 0:
            q = n // p
            if is_prime(q):
                return p, q
    return None

def main(filename):
    """Read an RSA number from a file and output its prime factorization."""
    try:
        with open(filename, 'r') as file:
            n = int(file.readline().strip())
            factors = factorize_rsa_number(n)
            if factors:
                print(f"{n} = {factors[0]} * {factors[1]}")
            else:
                print(f"Error: Cannot factorize {n} into prime numbers.")
                sys.exit(1)

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except ValueError:
        print("Error: Invalid number in the file.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa_factoring_challenge <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)


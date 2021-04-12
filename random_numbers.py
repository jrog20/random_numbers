"""
File: random_numbers.py
-----------------------
This program prints a series of random numbers in the
range from MIN_RANDOM to MAX_RANDOM, inclusive
"""

import random

MIN_RANDOM = 0
MAX_RANDOM = 100
NUM_RANDOM = 10

def main():
    """
    Print 10 random numbers between 0 - 100.
    """

    # random.seed (1)

    # Call to generate 10 random numbers
    for i in range(10):
        # Define range of random numbers
        NUM_RANDOM = random.randint(MIN_RANDOM, MAX_RANDOM)
        # Print 10 random numbers
        print(NUM_RANDOM)


if __name__ == '__main__':
    main()

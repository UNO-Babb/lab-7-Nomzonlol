#Project Euler Problem 1

import NumberTests

def largest_prime_factor(n):
    """Find the largest prime factor of a given number."""
    # Initialize the largest prime factor found so far
    largest_factor = 1
    
    # Handle any factors of 2 first
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    
    # Now n is odd, so we can start from 3 and increment by 2
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2
    
    # If n is a prime number greater than the largest factor found
    if n > largest_factor:
        largest_factor = n
    
    return largest_factor

# The number from the problem
number = 6008514751413

# Find and print the largest prime factor
result = largest_prime_factor(number)
print(f"The largest prime factor of {number} is: {result}")

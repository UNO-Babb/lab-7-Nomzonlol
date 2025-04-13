#Problem2.py
#Project Euler problem 2

from NumberTests import isEven
from NumberTests import fibonacciSequence

def sum_of_primes_below(limit):
    """
    Calculate the sum of all prime numbers below the given limit using the Sieve of Eratosthenes.
    
    Args:
        limit (int): Upper bound (exclusive) for prime numbers
        
    Returns:
        int: Sum of all primes below the limit
    """
    # Create a boolean array "is_prime[0..limit-1]" where is_prime[i] is True if i is prime
    is_prime = [True for i in range(limit)]
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    
    # Use Sieve of Eratosthenes to mark non-primes
    p = 2
    while p * p < limit:
        # If p is still marked as prime, mark all its multiples as non-prime
        if is_prime[p]:
            for i in range(p * p, limit, p):
                is_prime[i] = False
        p += 1
    
    # Sum all prime numbers
    prime_sum = sum(i for i in range(limit) if is_prime[i])
    
    return prime_sum

# Calculate the sum of all primes below two million
limit = 2000000
result = sum_of_primes_below(limit)
print(f"The sum of all primes below {limit} is: {result}")

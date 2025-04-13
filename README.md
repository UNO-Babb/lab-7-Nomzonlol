[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=19152394)
# Lab 7 - CIST 1600

One of my favorite "productive procrastination"  sites is [Project Euler](https://projecteuler.net/archives). The site has a series of math puzzles that require programming to solve. Python is a perfect tool for many of these problems and it is a great way to expand on your thinking about algorithms, coding techniques, and math.

Today we are going to look at several Project Euler problems, specifically thinking about how we could use problem deconstruction techniques to break the large problem into sub problems. Ideally we can use functions from earlier problems in later solutions.

### Your Assignment
- Write the ***isPrime*** function in the NumberTests and verify that it works.
- Pick 2-3 of the additional problems to solve using the functions in the NumberTests file.

### NumberTests.py
As you develop solutions, you should populate this file with some of the useful functions. I've started a few functions that might be useful.

#### isPrime(p)
Returns boolean (True/False) if the value given is prime.

#### isEven(n)
Returns boolean about given value being even.

#### addElement(list, num)
Adds the given number to the given list. Does not add duplicate values.

#### fibonacciSequence(value)
Returns a list of numbers in the Fibonacci sequence up to the given value

---
## Project Euler Problems
### Problem 3 - Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

---
### Problem 4 - Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

---
### Problem 7 - 10001st prime
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

---
### Problem 10 - Summation of primes
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

---
### Problem 21 - Amicable numbers
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

---
### Problem 23 - Non-abundant sums
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

---
### Problem 41 - Pandigital prime
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

---
### Problem 47 - Distinct primes factors
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7  
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23  
645 = 3 × 5 × 43  
646 = 2 × 17 × 19  

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

---
### Problem 50 - Consecutive prime sum
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

---
## Testing your code
You may not actually know that your code works until you fully test what you have written. It is often a good idea to get someone else to run your program, they may do something you had not anticipated which could show you a possible flaw or at least a design issue.

## End of class
- Add a commit message
- Commit to GitHub
- Sync work with Repo
- Submit your repo link to Canvas

# Print prime numbers in an array and sum of them

from array import *

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_and_sum(arr):
    primes = []
    sum_primes = 0
    for num in arr:
        if is_prime(num):
            primes.append(num)
            sum_primes += num
    return primes, sum_primes

arr = array('i', [])
arr.extend(map(int, input().split()))

primes, sum_primes = print_primes_and_sum(arr)

if not primes:
    print('-')
else:
    print(*primes)
    print(sum_primes)

#TESTED
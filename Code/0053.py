# Find largest prime element in an array

from array import *

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_largest_prime(arr):
    primes = [num for num in arr if is_prime(num)]
    if not primes:
        return -1
    return max(primes)

arr = array('i', [])
arr.extend(map(int, input().split()))

largest_prime = find_largest_prime(arr)

if largest_prime == -1:
    print('-')
else:
    print(largest_prime)

#TESTED
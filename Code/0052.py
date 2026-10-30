# Find avg of prime elements in an array

from array import *

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_avg_of_primes(arr):
    primes = [num for num in arr if is_prime(num)]
    if not primes:
        return -1
    return sum(primes) / len(primes)

arr = array('i', [])
arr.extend(map(int, input().split()))

avg = find_avg_of_primes(arr)

if avg == -1:
    print('-')
else:
    print(f"{avg:.2f}")

#TESTED
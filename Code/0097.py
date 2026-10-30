# Count in array have how many prime numbers using func

from array import *

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime(arr):
    count = 0
    for num in arr:
        if is_prime(num):
            count += 1
    return count

arr = array('i', [])
arr.extend(map(int, input().split()))

c = count_prime(arr)

print(c)

#TESTED
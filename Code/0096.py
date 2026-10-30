# Write func calc sum of all even elements in an array

from array import *

def sum_even_elements(arr):
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total

n = int(input())
arr = array('i', [])
arr.extend(map(int, input().split()))

print(sum_even_elements(arr))

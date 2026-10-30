# Calc sum of elements in even indexes of an array

from array import *

def sum_even_index_elements(arr):
    total = 0
    for i in range(0, len(arr), 2):
        total += arr[i]
    return total

n = int(input())
arr = array('i', [])
arr.extend(map(int, input().split()))

print(sum_even_index_elements(arr))

#TESTED
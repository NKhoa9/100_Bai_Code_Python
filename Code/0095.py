# Write func calc sum of all elements in an array

from array import *

def sum_array(arr):
    total = 0
    for num in arr:
        total += num
    return total

n= int(input())
arr = array('i', [])
arr.extend(map(int, input().split()))

print(sum_array(arr))

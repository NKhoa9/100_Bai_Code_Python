# Count pos elements in an array

from array import *

def count_positive_elements(arr):
    count = 0
    for num in arr:
        if num > 0:
            count += 1
    return count

n = int(input())
arr = array('i', [])
arr.extend(map(int, input().split()))

print(count_positive_elements(arr))
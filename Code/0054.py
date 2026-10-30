# Find largest negative element in an array

from array import *

def find_largest_negative(arr):
    negatives = [num for num in arr if num < 0]
    if not negatives:
        return -1
    return max(negatives)

arr = array('i', [])
arr.extend(map(int, input().split()))

largest_negative = find_largest_negative(arr)

if largest_negative == -1:
    print('-')
else:
    print(largest_negative)

#TESTED
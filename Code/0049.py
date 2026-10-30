# Find 1st largest element in an array and index of that largest element

from array import *

def find_first_largest(arr):
    largest = arr[0]
    index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            index = i
    return largest, index

n = int(input())
arr = array('i', [])
arr.extend(map(int, input().split()))

largest, index = find_first_largest(arr)

print(largest, index)

#TESTED
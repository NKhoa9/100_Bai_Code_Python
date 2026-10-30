# Find 2nd largest element in an array

from array import *

def find_second_largest(arr):
    unique_elements = list(set(arr))
    if len(unique_elements) < 2:
        return -1
    unique_elements.sort(reverse=True)
    return unique_elements[1]

arr = array('i', [])
arr.extend(map(int, input().split()))

second_largest = find_second_largest(arr)

if second_largest == -1:
    print('-')
else:
    print(second_largest)

#TESTED
# Find the 3rd smallest element in an array

from array import *

def find_third_smallest(arr):
    unique_elements = list(set(arr))
    if len(unique_elements) < 3:
        return -1
    unique_elements.sort()
    return unique_elements[2]

arr = array('i', [])
while True:
    try:
        arr.append(int(input()))
    except ValueError:
        break

third_smallest = find_third_smallest(arr)

if third_smallest == -1:
    print('-')
else:
    print(third_smallest)

#TESTED
# Find number x in an array

from array import *

def find_number(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

n, x = map(int, input().split())
arr = array('i', [])
arr.extend(map(int, input().split()))

result = find_number(arr, x)

if result != -1:
    print(f"Yes\n{result}")
else:
    print("No")

#TESTED
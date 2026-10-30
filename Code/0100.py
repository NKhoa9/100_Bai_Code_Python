# Write 2 funcs find max, min and position of them in array

from array import *

def find_max(arr):
    m = max(arr)
    index = 0
    for i in range(len(arr)):
        if arr[i] == m:
            index = i
            break

    return m, index

def find_min(arr):
    m = min(arr)
    index = 0
    for i in range(len(arr)):
        if arr[i] == m:
            index = i
            break

    return m, index

n = int(input())
arr = array('i', [])
arr.extend(map(int, input().split()))

print(*find_max(arr))
print(*find_min(arr))

#TESTED
# Sort an array in ascending order

from array import *

def sort_array(arr):
    sorted_arr = sorted(arr)
    return sorted_arr

n = int(input())
arr = array('i', [])
arr.extend(map(int, input().split()))

sorted_arr = sort_array(arr)

print(*sorted_arr)

#TESTED
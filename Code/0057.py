# Count number of different integers in an array

from array import *

def count_different_integers(arr):
    return len(set(arr))

arr = array('i', [])
while True:
    try:
        arr.append(int(input()))
    except ValueError:
        break

different_count = count_different_integers(arr)
print(different_count)

#TESTED
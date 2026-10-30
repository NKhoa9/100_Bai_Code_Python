# Count number of appearances of each integer in an array

from array import *

def count_integer_appearances(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict

n = int(input())
arr = array('i', [])
for _ in range(n):
    arr.append(int(input()))

appearances = count_integer_appearances(arr)
for num, count in appearances.items():
    print(f"{num} {count}")

#TESTED
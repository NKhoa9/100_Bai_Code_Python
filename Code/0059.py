# Find integer appears most frequently in an array

from array import *
def find_most_frequent_integer(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    most_frequent = max(count_dict, key=count_dict.get)
    return most_frequent, count_dict[most_frequent]

n = int(input())
arr = array('i', [])
for _ in range(n):
    arr.append(int(input()))

most_frequent_integer, frequency = find_most_frequent_integer(arr)
print(most_frequent_integer, frequency)

#TESTED
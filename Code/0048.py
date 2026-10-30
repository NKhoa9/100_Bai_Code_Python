# Print elements divisible by 5 in an array and sum of them

from array import *

def print_divisible_by_5(arr):
    divisible_by_5 = []
    sum_divisible_by_5 = 0
    for num in arr:
        if num % 5 == 0:
            divisible_by_5.append(num)
            sum_divisible_by_5 += num
    return divisible_by_5, sum_divisible_by_5

n = int(input())
arr = array('i', [])
arr.extend(map(int, input().split()))

divisible_by_5, sum_divisible_by_5 = print_divisible_by_5(arr)

if not divisible_by_5:
    print('-')
else:
    print(*divisible_by_5)
    print(sum_divisible_by_5)

#TESTED
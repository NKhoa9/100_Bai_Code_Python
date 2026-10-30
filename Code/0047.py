# Count and print lists of positive, negative elements in an array

from array import *

def count_positive_negative_elements(arr):
    count_positive = 0
    count_negative = 0
    positive_elements = []
    negative_elements = []
    for num in arr:
        if num > 0:
            count_positive += 1
            positive_elements.append(num)
        elif num < 0:
            count_negative += 1
            negative_elements.append(num)
    return count_positive, count_negative, positive_elements, negative_elements

n = int(input())
arr = array('i', [])
arr.extend(map(int, input().split()))

count_positive, count_negative, positive_elements, negative_elements = count_positive_negative_elements(arr)

print(count_positive, count_negative)
print(*positive_elements)
print(*negative_elements)

#TESTED
# Find avg of perfect squares in an array using func

from array import *
def is_perfect_square(num):
    if num < 0:
        return False
    root = int(num**0.5)
    return root * root == num

def find_avg_perfect_squares(arr):
    perfect_squares = [num for num in arr if is_perfect_square(num)]
    if not perfect_squares:
        return 0
    return sum(perfect_squares) / len(perfect_squares)

arr = array('i', [])
arr.extend(map(int, input().split()))

avg = find_avg_perfect_squares(arr)
if avg != 0:
    print(f"{avg:.1f}")
else:
    print('-')


# Check whether a number is a perfect square

n = int(input())

sqrt_n = int(n ** 0.5)
if sqrt_n * sqrt_n == n:
    print("Yes")
else:
    print("No")

#TESTED
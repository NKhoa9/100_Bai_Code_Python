# Find number of numbers divisible by 3

a = int(input())

n = 0
for i in range(1,a+1):
    if i%3==0:
        n += 1

print(n)

#TESTED
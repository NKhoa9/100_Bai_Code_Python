# Print 1st k prime numbers

k = int(input())

count = 0
num = 2

while count < k:
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=' ')
            count += 1
    num += 1

#TESTED
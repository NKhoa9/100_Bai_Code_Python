# Count prime numbers from m to n

m, n = map(int, input().split())

count = 0
for i in range(m, n + 1):
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            count += 1
print(count)

#TESTED
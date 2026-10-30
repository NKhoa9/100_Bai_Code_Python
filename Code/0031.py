# Count numbers divisible by 3 in range m to n

m, n = map(int, input().split())

count = 0
for i in range(m, n + 1):
    if i % 3 == 0:
        count += 1
print(count)

#TESTED
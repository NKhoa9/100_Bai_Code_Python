# Count numbers divisible by 3 or 5 in range m to n and find total sum of even numbers in that range

m, n = map(int, input().split())

count = 0
sum_even = 0
for i in range(m, n + 1):
    if i % 3 == 0 or i % 5 == 0:
        count += 1
    if i % 2 == 0:
        sum_even += i

print(count, sum_even)

#TESTED
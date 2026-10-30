# Calc avg of prime numbers from m to n

m, n = map(int, input().split())

prime_sum = 0
prime_count = 0

for i in range(m, n + 1):
    if i > 1:
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            prime_sum += i
            prime_count += 1

if prime_count > 0:
    average = prime_sum / prime_count
    print(f"{average:.2f}")
else:
    print('-')

#TESTED
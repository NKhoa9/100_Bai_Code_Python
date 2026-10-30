# Simplify factorial

m, n = map(int, input().split())

for i in range(1, min(m, n) + 1):
    if m % i == 0 and n % i == 0:
        m, n = m // i, n // i

print(f"{m}/{n}")
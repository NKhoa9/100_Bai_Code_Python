# Find GCD of 2 pos int a, b

a, b = map(int, input().split())

while b != 0:
    a, b = b, a % b # Euclidean algorithm: gcd(a,b)=gcd(b,a%b)

print(a)

#TESTED
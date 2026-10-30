# Write func find GCD

def gcd(a,b):
    while b != 0:
        a, b = b, a % b # Euclidean algorithm: gcd(a,b)=gcd(b,a%b)

    return a

a, b = map(int, input().split())
d = gcd(a,b)

print(f"{a//d}/{b//d}")

#TESTED
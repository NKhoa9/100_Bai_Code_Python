# Write func P(x.n) to calc x^n

def P(x,n):
    return x**n

def F(x,l):
    s = 0
    for i in l:
        s += i[0] * P(x, i[1])

    return s

k, x = map(int, input().split())
an = []

for _ in range(k):
    temp = list(map(int, input().split()))
    an.append(temp)

r = F(x,an)
print(r)

#TESTED
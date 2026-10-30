# Write func calc n!

def fact(n):
    r = 1
    for i in range(1,n+1):
        r = r*i

    return r

def calc_C(n,k):
    r = fact(n)/(fact(k)*fact(n-k))
    return r

m = int(input())
arr = [0]*m
for i in range(m):
    arr[i] = list(map(int, input().split()))

r = 0
for e in arr:
    n = e[0]
    k = e[1]
    r += calc_C(n,k)

print(int(r))

#TESTED
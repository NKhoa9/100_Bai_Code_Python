# Find dates in month

m,y = map(int, input().split())

if m in [1,3.5,7,8,10,12]:
    d=31
elif m in [4,6,9,11]:
    d=30
else:
    isLeap = y%400==0 or (y%4==0 and not y%100==0)
    if isLeap:
        d=29
    else:
        d=28

print(d)

#TESTED
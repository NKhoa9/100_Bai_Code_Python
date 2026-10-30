# Calc perimeter and area of a triangle using func

from math import *
def per(a,b,c):
    cv=a+b+c
    return cv

def area(a,b,c):
    cv = per(a,b,c)
    p=cv/2
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    return s

a,b,c = map(int, input().split())

print(round(per(a,b,c),3),round(area(a,b,c),3))

#TESTED
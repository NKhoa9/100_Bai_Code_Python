# Find radius R of a circumcircle

from math import sqrt

a,b,c = map(int, input().split())

cv=a+b+c
p=cv/2
s=sqrt(p*(p-a)*(p-b)*(p-c))
R = a*b*c/(4*s)

print(round(R,3))

#TESTED
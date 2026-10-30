# Find the perimeter and area of a triangle
from math import *

a,b,c = map(int, input().split())

cv=a+b+c
p=cv/2
s=sqrt(p*(p-a)*(p-b)*(p-c))

print(round(cv,3),round(s,3))

#TESTED
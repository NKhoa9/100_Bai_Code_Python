# Check whether a,b,c is 3 sides of a triangle

from math import *

a,b,c = map(int, input().split())

l = [a,b,c]
l.sort()
isTri = l[0]+l[1]-l[2] > 0
if not isTri:
    print("Day khong phai la 3 canh cua mot tam giac")
else:
    print("Day la 3 canh cua mot tam giac")
    cv=a+b+c
    p=cv/2
    s=sqrt(p*(p-a)*(p-b)*(p-c))
    print(round(cv,2),round(s,1))

#TESTED
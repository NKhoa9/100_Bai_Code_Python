# Find num divisible by 3

n = int(input())

l=[]
for i in range(1,n+1):
    if i%3==0:
        l += [i]

if len(l)==0:
    print('-')
else:
    print(*l, sep=' ')

#TESTED
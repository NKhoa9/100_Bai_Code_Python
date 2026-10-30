# Find max in 3 numbers

a,b,c = map(int, input().split())

if a==b==c:
    print('=')
else:
    print(max(a,b,c))

#TESTED
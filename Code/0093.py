# Using func find min of 2 num to find min of 3 num

def f_min(a,b):
    return min(a,b)

a,b,c = map(int, input().split())
print(f_min(f_min(a,b),c))

#TESTED
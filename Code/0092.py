# Using nested func

def add(a,b):
    return a+b

def div(a,b):
    return a/b

a,b,c = map(int, input().split())

print(f"{add(a,add(b,c))} {add(div(a,b),c):.2f} {div(a,add(b,c)):.3f}")

#TESTED
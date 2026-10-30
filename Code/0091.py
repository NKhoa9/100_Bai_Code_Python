# Write program using func to draw a rectangle w/ *

def dr(d,r):
    print('*'*d)
    for i in range(r-2):
        print(f'*{' '*(d-2)}*')
    print('*'*d)

d, r = map(int, input().split())

dr(d,r)
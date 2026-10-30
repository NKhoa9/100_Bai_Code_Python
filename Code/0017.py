# Calculate season

X = [2,3,4]
H = [5,6,7]
T = [8,9,10]
D = [11,12,1]

t = int(input())

if t in X:
    s = "Mua Xuan"
elif t in H:
    s = "Mua Ha"
elif t in T:
    s = "Mua Thu"
elif t in D:
    s = "Mua Dong"

print(s)

#TESTED
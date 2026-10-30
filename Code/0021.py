# Find taxi fee

km = int(input())

if km==1:
    c=12000
elif 2<=km<=30:
    c=12000+(km-1)*10000
else:
    c=12000+29*10000+(km-30)*9000

print(c)

#TESTED
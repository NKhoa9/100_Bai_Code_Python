# Calc electricity bill

kwh = int(input())

if kwh<=50:
    c=kwh*600
elif 51<=kwh<=100:
    c=50*600+(kwh-50)*800
elif 101<=kwh<=200:
    c=50*600+50*800+(kwh-100)*1100
else:
    c=50*600+50*800+100*1100+(kwh-200)*1500

print(c)

#TESTED
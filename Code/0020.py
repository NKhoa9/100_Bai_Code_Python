# Return change

N = int(input())

temp = N
_5 = temp//5000
temp = N - 5000*_5
_2 = temp//2000
temp = temp - 2000*_2
_1 = temp//1000

print(_5,_2,_1)

#TESTED
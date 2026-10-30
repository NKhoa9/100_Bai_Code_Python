# Find h m s

total_seconds = int(input())

h = total_seconds//3600
temp = total_seconds-3600*h
m = temp // 60
s = temp - 60*m


print(f"{h}:{m}:{s}")

#TESTED
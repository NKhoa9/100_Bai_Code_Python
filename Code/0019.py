# Find button? of vehicle plate

n = int(input())

temp = n
sum = 0
while temp != 0:
    digit = temp%10
    sum += digit
    temp = temp//10
isLucky = sum%10 == 9
if isLucky:
    msg = 'may man'
else:
    msg = 'chua may man'

print(f"{sum%10}\n{msg}")

#TESTED
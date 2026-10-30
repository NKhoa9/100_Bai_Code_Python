# Write func check if number divisible by 5

def isDivisible_5(n):
    if n%5 == 0:
        return True
    else:
        return False

n = int(input())

b = isDivisible_5(n)
if b == True:
    print("Yes")
else:
    print("No")

#TESTED
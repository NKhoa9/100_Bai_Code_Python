# Find sum of numbers divisible by 3 and 5

n= int(input())

sum=0
for i in range(1,n+1):
    if i%15==0:
        sum+=i

print(sum)

#TESTED
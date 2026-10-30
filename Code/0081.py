# Find place where char x last appears

s = input()
x = input()

index = -1
for i in range(len(s)):
    if s[i]==x:
        index = i

print(index)

#TESTED
# Find place where char x 1st appears

s = input()
x = input()

for i in range(len(s)):
    if s[i]==x:
        index = i
        break
    else:
        index = -1

print(index)

#TESTED
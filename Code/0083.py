# Count number of lowercase in a string

s = input()

count = 0
for c in s:
    if c.islower():
        count += 1

print(count)

#TESTED
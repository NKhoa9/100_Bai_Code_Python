# Count number of uppercase in a string

s = input()

count = 0
for c in s:
    if c.isupper():
        count += 1

print(count)

#TESTED
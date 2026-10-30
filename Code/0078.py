# Each character appear how many times in string

s = input()
s = s.lower()

dict = {}
for c in s:
    if c not in dict:
        dict[c] = 0
    else:
        dict[c] += 1

for char, count in dict.items():
    print(f"{char}:{count}", end = ' ')

#TESTED

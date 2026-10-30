# Find char appears most freq in a string

s = input().lower()

dict = {}
for c in s:
    if c not in dict:
        dict[c] = 1
    else:
        dict[c] += 1

m = max(dict, key=dict.get)

print(f"{m}:{dict[m]}")

#TESTED
# Convert 1st letter of each word in a string to capital

s = input()

temp = list(s)
for c in range(len(s)):
    if 1 <= c < len(s)-1 and temp[c] == ' ' and temp[c+1] != ' ':
        temp[c+1] = temp[c+1].upper()
    elif c == 0 and temp[c] != ' ':
        temp[c] = temp[c].upper()

s = ''.join(temp)
print(s)

#TESTED
# Reverse chars in each words

s = input()

temp = s.split()
temp2 = []
for c in temp:
    temp2.append(c[::-1])
              
s = ' '.join(temp2)
print(s)

#TESTED
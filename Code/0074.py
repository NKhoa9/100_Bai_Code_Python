# Reverse words in sentence

s = input()

temp = s.split()
temp = temp[::-1]
temp = ' '.join(temp)

print(temp)

#TESTED
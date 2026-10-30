# Delete extra space in the middle of string only

s = input()

def find_l(s):
    l = ""
    for i in range(len(s)):
        if s[i] != ' ':
            break
        else:
            l += s[i]
    return l

def find_r(s):
    r = ""
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            break
        else:
            r += s[i]
    return r

def find_m(s):
    s = ' '.join(s.split())
    return s

l = find_l(s)
r = find_r(s)
m = find_m(s)

o = l + m + r
print(o)

#TESTED
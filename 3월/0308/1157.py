# 백준 1157번

from string import ascii_uppercase
alphabet_list = list(ascii_uppercase)

n = input().upper()
c = 0
for a in alphabet_list:
    temp = n.count(a)
    if c < temp:
        c = temp
        result = a
    elif c == temp:
        c = temp
        result = '?'
print(result)

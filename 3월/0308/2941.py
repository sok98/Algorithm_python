# 2941번

a = input()
cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in cro:
    a = a.replace(i, "#")

print(len(a))

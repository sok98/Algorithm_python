N = int(input())
s = []
s_min = []
f = []
f_min = []
for n in range(N):
    start, finish = input().split(" ~ ")
    s.append(list(map(int, start.split(":"))))
    f.append(list(map(int, finish.split(":"))))
    s_min.append(s[n][0] * 60 + s[n][1])
    f_min.append(f[n][0] * 60 + f[n][1])

if max(s_min) > min(f_min):
    print(-1)
else:
    print('{0:02d}:{1:02d} ~ {2:02d}:{3:02d}'.format(
        max(s_min)//60, max(s_min) % 60, min(f_min)//60, min(f_min) % 60))

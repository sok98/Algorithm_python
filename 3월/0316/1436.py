N = int(input())
movie = []

for a in range(10000):
    if a % 1000 == 666:
        for i in range(1000):
            movie.append(a*1000+i)
    elif a % 100 == 66:
        for i in range(100):
            movie.append(a*1000+600+i)
    elif a % 10 == 6:
        for i in range(10):
            movie.append(a*1000+660+i)
    else:
        movie.append(a * 1000 + 666)

print(movie[N-1])

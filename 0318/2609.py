n, m = map(int, input().split())

div = 0
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        if m % (n / i) == 0:
            div = n // i
            break
        elif m % i == 0:
            if div < i:
                div = i

mul = n
while mul % m != 0:
    mul += n

print(div)
print(mul)

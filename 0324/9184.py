answer = []
dp = {}


def w(a, b, c):
    abc = str(a) + "/" + str(b) + "/" + str(c)
    if abc in dp:
        return dp[abc]

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if a < b and b < c:
        dp[abc] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[abc]
    else:
        dp[abc] = w(a-1, b, c) + w(a-1, b-1, c) + \
            w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return dp[abc]


while 1:
    a, b, c = list(map(int, input().split()))
    if a == -1 and b == -1 and c == -1:
        break
    else:
        a = 'w({0}, {1}, {2}) = {3}'.format(a, b, c, w(a, b, c))
        answer.append(a)

for a in answer:
    print(a)

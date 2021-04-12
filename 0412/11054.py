import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

inc = [1] * N
dec = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j] and inc[i] <= inc[j]:
            inc[i] = 1 + inc[j]

for i in range(N-1, -1, -1):
    for j in range(N - 1, i, -1):
        if A[i] > A[j] and dec[i] <= dec[j]:
            dec[i] = 1 + dec[j]

answer = [sum(s)-1 for s in zip(inc, dec)]
print(max(answer))


# def check():
#     for n in range(N, 2):
#         for i in combinations(A, n):
#             change = False
#             success = True
#             for j in range(1, n):
#                 if i[n - 1] > i[n]:
#                     change = True
#                 else:
#                     if change == True:
#                         success = False
#                         break
#             if success == True:
#                 return n


# print(check())

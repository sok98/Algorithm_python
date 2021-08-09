import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
button = list(input().split())

answer = abs(N-100)    # +,-로만 이동 횟수

if 100 == N:
    print(0)

else : 
    for count in range(100001):
        ok = True
        for i in str(N+count):
            if i in button:
                ok = False
                break
        if ok == True:
            print(min(answer, count + len(str(N+count))))
            break
        
        if N-count >= 0:
            ok = True
            for i in str(N-count):
                if i in button:
                    ok = False
                    break
            if ok == True:
                print(min(answer, count + len(str(N-count))))
                break
        

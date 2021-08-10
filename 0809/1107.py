import sys
input = sys.stdin.readline

button = []

N = int(input())
M = int(input())
if M != 0:
    button.extend(list(map(str, input().split())))

answer = abs(N-100)    # +,-로만 이동 횟수

if 100 == N:    # 이동하려는 채널이 현재 있는 채널인 경우
    print(0)
    
elif M == 10: # 모든 숫자 버튼이 고장난 경우 : +,-로만 이동
    print(answer)

else : 
    for count in range(1000001):
        if N-count >= 0:
            ok = True
            for i in str(N-count):
                if i in button:
                    ok = False
                    break
            if ok == True:
                print(min(answer, count + len(str(N-count))))
                break
        
        ok = True
        for i in str(N+count):
            if i in button:
                ok = False
                break
        if ok == True:
            print(min(answer, count + len(str(N+count))))
            break
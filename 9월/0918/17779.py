import sys
input = sys.stdin.readline

N = int(input())
area = []
for _ in range(N):
    area.append(list(map(int, input().split())))

answer = 100*20*20  # 인구 차이의 최대값으로 리셋

# 기준점 (x, y) : 0 <= x < N-2, 1 <= y < N-1
for x in range(0, N-2):
    for y in range(1, N-1):
        
        # 경계의 길이 d1, d2 : 1 <= d1 <= y, 1 <= d2 <= N-y
        for d1 in range(1, y+1):
            for d2 in range(1, N-y+1):                
                if 0 <= y-d1 and y+d2 < N and x+d1+d2 < N:  # 인덱스 체크

                    cnt = [0, 0, 0, 0, 0]   # 1 ~ 5 구역 인구수 0으로 리셋
                    
                    # 확인할 구역 (r, c)
                    for r in range(N):
                        for c in range(N):
                            population = area[r][c]
                            
                            if r < x+d1 and c <= y:         # 1 선거구
                                if r+c >= x+y:
                                    cnt[4] += population
                                else:
                                    cnt[0] += population
                            
                            elif r <= x+d2 and y < c:       # 2 선거구
                                if r-c >= x-y:
                                    cnt[4] += population
                                else:
                                    cnt[1] += population
                            
                            elif x+d1 <= r and c < y-d1+d2: # 3 선거구
                                if r-c <= x-y+(2*d1):
                                    cnt[4] += population
                                else:
                                    cnt[2] += population
                            
                            elif x+d2 < r and y-d1+d2 <= c: # 4 선거구
                                if r+c <= x+y+(2*d2):
                                    cnt[4] += population
                                else:
                                    cnt[3] += population
                            
                            else:
                                cnt[4] += population
                    
                    answer = min(answer, max(cnt)-min(cnt))
                
                else:   # area를 벗어나는 경우
                    break

print(answer)
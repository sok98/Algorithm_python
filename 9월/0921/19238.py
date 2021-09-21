import sys
input = sys.stdin.readline

# N, M, 초기 연료 양 입력
N, M, fuel = map(int, input().split())

# 활동 영역 지도 area 입력
area = [[1 for _ in range(N+1)]]
for _ in range(N):
    area.append([1])
    area[-1].extend(list(map(int, input().split())))

# 운전을 시작하는 칸 now 입력
now = tuple(map(int, input().split()))

# 승객의 출발지와 목적지 입력
passenger = {}
for _ in range(M):
    a, b, c, d = map(int, input().split())
    passenger[(a, b)] = (c, d)

around = [(0,1), (1,0), (-1,0), (0,-1)]

take_a_taxi = False

while passenger:
    arrival, target = tuple(), set()
    visited, queue = set(), {now}
    move = 0
    
    while queue:
        candidate = set()
        for x, y in queue:
            if (0 <= x < N+1 and 0 <= y < N+1) and area[x][y] == 0:
                if take_a_taxi and (x, y) == passenger[now]:
                    del passenger[now]
                    arrival = (x, y)
                    break
                
                elif not take_a_taxi and (x, y) in passenger:
                    target.add((x, y))
                
                else:
                    for _x, _y in around:
                        if (x+_x, y+_y) not in visited:
                            candidate.add((x+_x, y+_y))
        
            visited.add((x, y))
            
        if arrival:
            take_a_taxi = False
            now = arrival
            fuel = fuel + move if fuel >= move else -1
            break

        if target:
            take_a_taxi = True
            now = sorted(target)[0]
            fuel -= move
            break
            
        if not candidate:
            fuel = -1
            break
        
        queue = candidate
        move += 1

    if fuel < 0:
        fuel = -1
        break

        

print(fuel)
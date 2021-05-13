import sys
input = sys.stdin.readline

N = int(input())
video = []
for _ in range(N):
    line = input().rstrip()
    video.append(line)


def check(start1, end1, start2, end2):
    part1 = [[start1, start1 + (end1-start1) // 2],
             [start1 + (end1-start1) // 2, end1]]
    part2 = [[start2, start2 + (end2-start2) // 2],
             [start2 + (end2-start2) // 2, end2]]

    result = "("

    for a in part1:
        for b in part2:
            diff = False
            bfr = video[a[0]][b[0]]  # 첫번째 값 저장
            for i in range(a[0], a[1]):
                for j in range(b[0], b[1]):
                    if bfr != video[i][j]:  # 모두 같은지 확인
                        diff = True
                        break
                if diff == True:    # 다른 숫자 발견, 재귀 호출
                    bfr = check(a[0], a[1], b[0], b[1])
                    break
            result += str(bfr)

    result += ")"
    return result


answer = check(0, N, 0, N)
# 모두 같은 숫자로만 되어있을 때 괄호없이 숫자만 answer에 저장
if len(answer) == 6 and answer[1] == answer[2] == answer[3] == answer[4]:
    answer = answer[1]
print(answer)

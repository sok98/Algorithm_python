def solution(weights, head2head):
    # 선수번호 : [승리 횟수(나중에 승률로 바뀜), 무거운 사람 승리 횟수, 자기 몸무게]
    player = { i+1:[0.0, 0, weights[i]] for i in range(len(weights)) }   

    for idx, score in enumerate(head2head):
        cnt = 0
        for i, s in enumerate(score):
            if s != "N": cnt += 1   # 대결 횟수 -1
            if s == "W":
                player[idx+1][0] += 1   # 승리 횟수 +1
                if weights[idx] < weights[i]:
                    player[idx+1][1] += 1   # 더 무거운 사람 승리 횟수 +1
        player[idx+1][0] = player[idx+1][0] / cnt * 100 if cnt != 0 else 0

    player = sorted(player.items(), key=lambda x:(x[1], -x[0]), reverse=True)
    answer = [i[0] for i in player]

    return answer


print(solution([60,70,60], ["NNN","NNN","NNN"]))
print(solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"]))
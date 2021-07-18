def solution(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            finish = 0
            for i in range(len(progresses)):
                if progresses[i] >= 100:
                    finish += 1
                    progresses[i] = -1
                    speeds[i] = -1
            answer.append(finish)
            while -1 in progresses:
                progresses.remove(-1)
                speeds.remove(-1)
            print(progresses)

    return answer


print(solution([93, 30, 55], [5, 70, 5]))

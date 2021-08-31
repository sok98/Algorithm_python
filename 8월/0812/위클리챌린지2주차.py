def solution(scores):
    answer = ''
    d = len(scores)

    new_scores = [[i[j] for i in scores] for j in range(d)]

    for i, std in enumerate(new_scores):
        n = std[i]
        if std.count(n) == 1 and (max(std) == n or min(std) == n):
            avg = (sum(std)-n) / (d-1)
        else:
            avg = sum(std) / d

        if avg >= 90:
            answer += 'A'
        elif avg >= 80:
            answer += 'B'
        elif avg >= 70:
            answer += 'C'
        elif avg >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer
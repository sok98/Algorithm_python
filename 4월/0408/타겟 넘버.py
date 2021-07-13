def solution(numbers, target):
    answer = 0

    sum = [[] for _ in range(len(numbers))]
    sum[0].append(numbers[0])
    sum[0].append(-numbers[0])

    for i in range(1, len(numbers)):
        for k in sum[i - 1]:
            sum[i].append(k + numbers[i])
            sum[i].append(k - numbers[i])

    return sum[len(numbers)-1].count(target)


print(solution([1, 1, 1, 1, 1], 3))

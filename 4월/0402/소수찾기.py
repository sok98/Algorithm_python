import itertools


def solution(numbers):
    answer = {}
    numbers = list(numbers)

    # 큰 수부터 정렬
    numbers.sort(reverse=True)

    # 가장 큰 수 조합
    max_number = ""
    for i in numbers:
        max_number += str(i)
    max_number = int(max_number)

    # 소수 True로 저장하기
    idx = [True for i in range(max_number + 1)]
    idx[0] = False
    idx[1] = False
    for i in range(2, int(max_number**0.5)+1):
        if idx[i]:
            for j in range(2*i, max_number+1, i):
                idx[j] = False

    print(numbers)
    for i in range(1, len(numbers)+1):
        target = list(map(''.join, itertools.permutations(numbers, i)))
        for j in target:
            if int(j) not in answer:
                answer[int(j)] = idx[int(j)]

    result = 0
    for v in answer.values():
        if v == True:
            result += 1
    return result


print(solution("011"))

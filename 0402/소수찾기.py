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
    print("max_number---", max_number)

    # 소수 True로 저장하기
    idx = [True for i in range(max_number + 1)]
    idx[0] = False
    idx[1] = False
    for i in range(2, int(max_number**0.5)+1):
        if idx[i]:
            for j in range(2*i, max_number+1, i):
                idx[j] = False

    # # 숫자 조합찾기
    # def combi(n, exp):
    #     if len(str(n)) > len(numbers):
    #         print("len(str(n) : ", len(str(n)),
    #               "len(numbers) : ", len(numbers))
    #         return
    #     print("int(n)", int(n))
    #     print("idx[int(n)]", idx[int(n)])
    #     answer[int(n)] = idx[int(n)]
    #     for i in numbers:
    #         if i.index not in exp:
    #             exp_copy = exp
    #             exp_copy.append(i.index)
    #             combi(int(str(n)+i), exp_copy)

    # for i in numbers:
    #     combi(i, [i.index])

    result = 0
    for v in answer.values():
        if v == True:
            result += 1
    return result


print(solution("011"))

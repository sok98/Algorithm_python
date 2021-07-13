def solution(n, lost, reserve):

    d_lost = list(set(lost) - set(reserve))
    d_reserve = list(set(reserve) - set(lost))

    for i in d_lost:
        if i + 1 in d_reserve:
            d_reserve.remove(i + 1)

        elif i - 1 in d_reserve:
            d_reserve.remove(i - 1)
        else:
            n = n-1

    return n


print(solution(3, [1, 2], [2, 3]))

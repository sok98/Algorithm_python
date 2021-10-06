def solution(sizes):
    return max(max(s) for s in sizes)*max(min(s) for s in sizes)


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]	))
def solution(numbers):
    
    #numbers 재배열
    numbers_str = [str(n) for n in numbers]
    numbers_str.sort(key = lambda x: (x*4)[:4], reverse = True)

    if numbers_str[0] == "0":
        return "0"
    else:
        return "".join(numbers_str)


print(solution([12, 121]))
print(solution([0,0,0,0]))
# print(solution([3, 30, 34, 5, 53, 9]))
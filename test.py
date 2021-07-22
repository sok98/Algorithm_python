def solution(numbers):

    num_str = [str(num) for num in numbers]

    num_str.sort(key = lambda x: (x*4)[:4], reverse = True)
    print(num_str)

    if num_str[0] != 0:
        answer = "".join(num_str)
        return answer
    else:
        return "0"


print(solution([3, 30, 34, 5, 53, 9]))
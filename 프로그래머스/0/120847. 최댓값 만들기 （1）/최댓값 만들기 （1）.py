def solution(numbers):
    num = sorted(numbers)
    answer = num[-1]*num[-2]
    return answer
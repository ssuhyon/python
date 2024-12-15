def solution(n):
    lst = list(range(1, n + 1))
    result = []
    for i in lst:
        if i % 2 != 0:
            result.append(i)
    return result


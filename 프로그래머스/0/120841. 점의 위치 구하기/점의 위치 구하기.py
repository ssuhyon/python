def solution(dot):
    a, b = dot
    if a > 0:
        if b > 0:
            answer = 1
        else:
            answer = 4
    if a < 0:
        if b > 0:
            answer = 2
        else:
            answer = 3
    return answer
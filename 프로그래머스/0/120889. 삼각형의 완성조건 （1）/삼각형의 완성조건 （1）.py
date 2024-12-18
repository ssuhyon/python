def solution(sides):
    a = sorted(sides)
    if a[0] + a[1] <= a[2]:
        answer = 2
    else:
        answer = 1
    return answer
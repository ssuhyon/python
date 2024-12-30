def solution(names):
    answer = []
    num = len(names)
    for i in range(num):
        if i == 0:
            answer.append(names[i])
        elif i%5 == 0:
            answer.append(names[i])
    return answer
def solution(arr, n):
    answer = []
    if len(arr)%2==1:
        for i,j in enumerate(arr):
            if i%2==0:
                answer.append(j + n)
            else:
                answer.append(j)
    else:
        for x, y in enumerate(arr):
            if x%2==1:
                answer.append(y + n)
            else:
                answer.append(y)
    return answer

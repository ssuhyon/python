def solution(array, height):
    if not (1<=len(array) <=100):
        raise ValueError
    if not all(1<=value<=200 for value in array) or not (1<= height<=200):
        raise ValueError
    answer = sum(1 for value in array if value > height)
    return answer
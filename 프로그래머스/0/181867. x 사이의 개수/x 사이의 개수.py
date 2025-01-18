def solution(myString):
    split_strings = myString.split('x')
    answer = [len(segment) for segment in split_strings]
    return answer
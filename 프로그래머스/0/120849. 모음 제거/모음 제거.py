def solution(my_string):
    moum = 'aeiouAEIOU'
    answer = my_string
    for x in moum:
        answer = answer.replace(x,'')
    return answer
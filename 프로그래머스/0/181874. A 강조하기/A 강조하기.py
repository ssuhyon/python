def solution(myString):
    myString = myString.replace('a','A')
    answer = ''
    for i in myString:
        if i == 'A':
            answer +='A'
        else:
            answer += i.lower()
    return answer
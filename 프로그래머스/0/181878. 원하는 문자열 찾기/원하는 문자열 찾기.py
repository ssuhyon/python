def solution(myString, pat):
    a = myString.lower()
    b = pat.lower()
    return int(b in a)
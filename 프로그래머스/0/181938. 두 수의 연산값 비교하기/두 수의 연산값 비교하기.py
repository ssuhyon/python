def solution(a, b):
    x = str(a)
    y = str(b)
    if int(x+y)>int(2*a*b):
        return int(x+y)
    elif int(x+y)<int(2*a*b):
        return int(2*a*b)
    else:
        return int(a+b)
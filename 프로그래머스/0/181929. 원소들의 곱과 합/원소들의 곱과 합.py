def solution(num_list):
    x = 1
    y = sum(num_list)**2
    for i in num_list:
        x *= i
    return 1 if x<y else 0
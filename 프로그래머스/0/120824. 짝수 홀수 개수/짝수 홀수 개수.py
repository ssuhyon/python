def solution(num_list):
    zzag = 0
    hol = 0
    for i in num_list:
        if i % 2 == 0:
            zzag += 1
        else:
            hol += 1
    return [zzag, hol]
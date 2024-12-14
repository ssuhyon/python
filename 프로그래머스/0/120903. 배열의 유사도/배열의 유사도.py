def solution(s1, s2):
    common = set(s1) & set(s2)
    if common:
        return len(list(common))
    else:
        return 0
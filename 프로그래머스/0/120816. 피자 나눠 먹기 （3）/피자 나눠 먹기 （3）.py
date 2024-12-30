def solution(slice, n):
    if n > slice:
        if n % slice == 0:
            return n//slice
        return n//slice + 1
    return 1
        
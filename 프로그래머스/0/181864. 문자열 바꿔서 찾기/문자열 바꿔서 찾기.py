def solution(myString, pat):
    swapped = ''.join('A' if char == 'B' else 'B' for char in myString)
    return 1 if pat in swapped else 0
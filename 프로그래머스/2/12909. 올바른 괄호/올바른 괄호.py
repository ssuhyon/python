def solution(s):
    # 조건 1: 처음이 ')' 또는 마지막이 '('인 경우 False
    if s[0] == ')' or s[-1] == '(':
        return False

    # 조건 2: 괄호의 균형을 확인
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1

        # 조건 3: count가 음수가 되면 False
        if count < 0:
            return False

    # 조건 4: 최종적으로 count가 0이어야 True
    return count == 0

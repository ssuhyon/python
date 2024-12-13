def solution(n):
    # n x n 크기의 0으로 초기화된 배열 생성
    matrix = [[0] * n for _ in range(n)]
    # 방향 벡터: 오른쪽, 아래, 왼쪽, 위
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0  # 현재 방향 (오른쪽)
    row, col = 0, 0  # 시작 위치
    value = 1  # 배열에 채울 값
    
    while value <= n * n:
        # 현재 위치에 값 채우기
        matrix[row][col] = value
        value += 1
        
        # 다음 위치 계산
        next_row = row + directions[current_direction][0]
        next_col = col + directions[current_direction][1]
        
        # 다음 위치가 경계를 벗어나거나 이미 채워진 경우 방향 전환
        if (
            next_row < 0 or next_row >= n or
            next_col < 0 or next_col >= n or
            matrix[next_row][next_col] != 0
        ):
            current_direction = (current_direction + 1) % 4  # 다음 방향으로 전환
        
        # 다음 위치로 이동
        row += directions[current_direction][0]
        col += directions[current_direction][1]
    
    return matrix

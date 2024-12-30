def solution(num_list):
    even = 0
    odd = 0

    for idx, value in enumerate(num_list):
        if idx % 2 == 0:
            even += value
        else:
            odd += value

    return max(even, odd)
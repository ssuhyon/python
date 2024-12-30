def solution(num_list):
    odd_str = ""
    even_str = ""
    
    for i in num_list:
        if i % 2 != 0:  # 홀수인 경우
            odd_str += str(i)
        else:           # 짝수인 경우
            even_str += str(i)
    
    odd_num = int(odd_str) if odd_str else 0  # 홀수 문자열을 숫자로 변환
    even_num = int(even_str) if even_str else 0  # 짝수 문자열을 숫자로 변환
    
    return odd_num + even_num
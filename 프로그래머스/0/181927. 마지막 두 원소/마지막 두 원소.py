def solution(num_list):
    y = num_list[-2]
    z = num_list[-1]
    if z > y:
        num_list.append(z - y)
    else:
        num_list.append(2 * z)
    return num_list
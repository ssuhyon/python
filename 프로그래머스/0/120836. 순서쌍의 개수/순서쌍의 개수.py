def solution(n):
    count = 0
    pairs = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            pairs.append((i, n//i))
            count +=1
            if i != n//i:
                count += 1
    return count
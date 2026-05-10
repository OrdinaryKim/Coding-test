def solution(n, k):
    if n > 10:
        services = (n // 10) * 2000
    else:
        services = 0
    answer = (n * 12000) + (k * 2000) - services
    return answer
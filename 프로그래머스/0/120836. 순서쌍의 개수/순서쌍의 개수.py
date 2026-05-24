def solution(n):
    answer = 0
    # 1부터 n의 제곱근까지 반복
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            answer += 1
            
    # 제곱근의 제곱이 n(완전제곱수)인 경우 중복 제거, 아니면 2배
    return answer * 2 if (n**0.5) != int(n**0.5) else answer * 2 - 1
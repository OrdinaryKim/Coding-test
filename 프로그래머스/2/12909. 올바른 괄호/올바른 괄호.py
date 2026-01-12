def solution(s: str) -> bool:
    bol = 0  # 현재까지 '(' 개수 - ')' 개수

    for ch in s:
        if ch == '(':
            bol += 1
        else:  # ch == ')'
            bol -= 1
            if bol  < 0:      # 닫는 괄호가 먼저 나오면 즉시 실패
                return False

    return bol == 0          # 모두 처리 후 남은 '('가 없으면 성공
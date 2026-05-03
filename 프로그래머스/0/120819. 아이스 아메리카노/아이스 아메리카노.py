def solution(money):
    cup = money // 5500
    hay = money % 5500
    answer = [cup, hay]
    return answer
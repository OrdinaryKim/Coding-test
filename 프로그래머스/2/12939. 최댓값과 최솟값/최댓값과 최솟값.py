def solution(s: str) -> str:
    it = map(int, s.split())
    mn = mx = next(it)
    for x in it:
        if x < mn: mn = x
        if x > mx: mx = x
    return f"{mn} {mx}"
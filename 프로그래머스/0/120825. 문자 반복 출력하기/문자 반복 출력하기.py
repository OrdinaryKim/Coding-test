def solution(my_string, n):
    string = ''
    
    for ch in my_string:
        string += ch * n
    
    return string
def solution(list):
    value = False
    lst = "".join(list)
    if lst == lst[::-1]:
        value = True
    return value

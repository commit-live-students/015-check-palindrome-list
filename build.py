def solution(lst):
    '''
    Enter your code here
    '''
    if lst == lst[::-1]:
        value = True
    else:
        value = False
    return value

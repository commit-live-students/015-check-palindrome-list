def solution(list_in):
    '''
    Enter your code here
    '''
    equal = []
    for i in range(len(list_in)):
        if list_in[i] == list_in[-(i+1)]:
            continue
        else:
            return False
    return True

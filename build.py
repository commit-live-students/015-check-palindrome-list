def solution(input_list):
    '''
    Enter your code here
    '''
    value = True
    for index, elm in enumerate(input_list):
        if input_list[index] != input_list[len(input_list)-index-1]:
            value=False
    return value

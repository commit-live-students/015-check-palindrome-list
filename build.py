import copy
def solution(list):
    '''
    Enter your code here
    '''
    value = True
    inputList = copy.copy(list)
    list.reverse()
    print inputList
    print list
    if(inputList == list):
        return value
    else:
        value = False
        return value
    #return value

solution([1,2,3])

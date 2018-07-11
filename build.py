def solution(list):
    '''
    Enter your code here
    '''
    ogList = list
    newList = ogList[::-1]
    print ogList
    print newList
    if ogList == newList:
        value = True
    else:
        value = False
    return value

print solution(['a','b','c','b','a'])

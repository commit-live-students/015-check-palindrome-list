def solution(list):
    '''
    Enter your code here
    '''
    if list[::-1] == list:
       return True
    else:
       return False

output = solution(["a","c","b","c","a"])
print output

def solution(list):
    return True if list==list[::-1] else False


l = (1,6,4,6,1)
print solution(l)

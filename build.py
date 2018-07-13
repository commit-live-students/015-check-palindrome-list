def solution(list):
    '''
    Enter your code here
    '''
    i, j = 0, len(list)
    mid = int(j/2)
    isPallindrome = True

    while i <= mid:
        if list[i] == list[j-1-i]:
            i += 1
        else:
            isPallindrome = False
            break

    return isPallindrome

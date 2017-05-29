def solution(list):
    '''
    Enter your code here
    '''
    i, n = 0, len(list)
    mid = int(n/2)
    isPallindrome = True
    while i <= mid:
        if list[i] == list[n-1-i]:
            i += 1
        else:
            isPallindrome = False
            break

    return isPallindrome


print(solution([1,3,3,3,2,1]))

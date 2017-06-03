def solution(l):
    reverse = list(reversed(l))
    if l==reverse:
        print "Palindrome"
        return True
    else:
        print "not palindrome"
        return False
solution([1,2,3,2,1])

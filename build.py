def solution(l):
    list1 = list(l)
    list1.reverse()
    if l == list1:
        return True
    else:
        return False

print solution(['n','i','t','m','n'])

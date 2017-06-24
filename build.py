def solution(lis):
    rev_lis = list(reversed(lis))
    for i in range(0, len(lis)):
        if (lis[i] != rev_lis[i]):
            return False
    return True

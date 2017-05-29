def solution(list):

    isPallidrome = True
    for x in list:
        if x == list[-1]:
            list = list[:-1]
        else:
            isPallidrome = False
            break
    return isPallidrome

print solution('abccba')

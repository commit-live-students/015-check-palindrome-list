def solution(list):
    flag=0
    r=list[::-1]
    for i in range(0, len(list)-1):
        if r[i] == list[i]:
            flag = 1
        else:
            flag = 0
    return flag

print solution([3,2,3])

def solution(list):
    n=len(list)-1
    flag=True
    for i in range(0,int(n/2)):
        if(list[i]!=list[n-i]):
            return False
    return True

print(solution([1,2,3,4,3,'f',2,1]))

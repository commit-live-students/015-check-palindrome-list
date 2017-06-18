def solution(in_list):
    in_list  = list(in_list)
    cmp = list(in_list)
    in_list.reverse()
    print("Original list gets reversed ",in_list)
    print("Copy of list is ",cmp)
    isPal = True
    for i in range(0,len(in_list)):
        if(in_list[i]!=cmp[i]):
            isPal = False
            break
    print isPal
    return isPal

solution('NITI')

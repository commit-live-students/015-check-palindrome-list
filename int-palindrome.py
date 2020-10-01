def solution(list):
    # creating an empty list 
    lst = [] 
    
    # number of elemetns as input 
    n = int(input("Enter number of elements : ")) 
    
    # iterating till the range 
    for i in range(0, n): 
        ele = int(input())
    
        lst.append(ele) # adding the element

    out_list = lst[::-1] #reversing a list
    m=0
    for i in range(0,n):
        if lst[i]==out_list[i]:
            m=m+1
        else:
            print("FALSE")
            break
    if m==n:
        print("TRUE")
            

            
    

solution(list)
        

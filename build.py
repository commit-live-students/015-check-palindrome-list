def solution(user_list):
    pal_list = []

    for i in range(len(user_list)-1,-1,-1):
                pal_list.append(user_list[i])
    if pal_list == user_list:
        return True
    else:
        return False

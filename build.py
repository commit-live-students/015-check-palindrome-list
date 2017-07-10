
def solution(my_list):
    if len(my_list) <= 1:
        return True
    else:
        if my_list[0] == my_list[-1]:
            return solution(my_list[1:-1])
        else:
            return False
my_list=['n','i','t','i','n']
solution(my_list)

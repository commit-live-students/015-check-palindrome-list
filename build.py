ls= ['n','i','t','i','n']
def solution(ls):

    if ls == ls[::-1]:
        value = True
    else:
        value = False

    return value

# solution(ls)
# Output : True

# solution(['n', 'i', 't', 'i', 'b', 'n'])
# Output : False

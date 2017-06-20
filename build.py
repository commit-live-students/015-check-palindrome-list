def solution(list):
    palindrome = list[::-1]
    value = None
    if palindrome == list:
        value = True
    else:
        value = False
    return value

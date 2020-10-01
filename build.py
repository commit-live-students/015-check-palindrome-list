def solution(list):
    if list == list[::-1]:
        value = "Yes it is a palindrome list"
    else:
        value = "No it is not a palindrome list"
    return value


if __name__ == " __main__":
    n = input("Enter how many items you want in your list --> ")
    input_list = []
    for i in range(int(n)):
        list_items = input(f"Enter item {i+1} of list --> ")
        input_list.append(list_items)

    print(solution(input_list))

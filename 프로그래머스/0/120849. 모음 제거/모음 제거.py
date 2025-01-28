def solution(my_string):
    for str in my_string:
        for v in ['a', 'e', 'i', 'o', 'u']:
            if str == v:
                my_string = my_string.replace(str, '')
    return my_string
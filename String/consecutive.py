def get_non_repeating_character(get_string, size, start, second, flag=0):
    if second > size or flag == 1:
        if flag == 1:
            second = start+1
            return get_non_repeating_character(get_string, size, start+1, second)
        if start > size:
            return 
        else:
            return get_string[start]
    else:
        if get_string[start] == get_string[second]:
            return get_non_repeating_character(get_string, size, start, second, flag=1)
        else:
            return get_non_repeating_character(get_string, size, start, second+1, flag=0)    
        
get_string = "hello"
size = len(get_string)-1
start = 0
second = 1
print(get_non_repeating_character(get_string, size, start, second))  
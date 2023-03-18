def get_first_non_repeating(get_string, start, second, size, flag=0):
    if second > size or flag == 1:
        if start > size-1:
            return 
        if flag == 1:
            start += 1
            second = start + 1
            return get_first_non_repeating(get_string, start, second, size, flag=0)
        else:
            return get_string[start]
    else:
        if get_string[start] == get_string[second]:
            return get_first_non_repeating(get_string, start+1, second+1, size, flag=1)
        else:
            return get_first_non_repeating(get_string, start, second+1, size, flag=0)    
        
get_string = "hholl"
start = 0
second = 1
size = len(get_string)-1
print("the first non repeating charatcer is : ", get_first_non_repeating(get_string, start, second, size))        
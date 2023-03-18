def get_non_repeating_substring(get_string, start, second, size):
    if second > size:
        if start > size - 1:
            return get_string
        else:
            start += 1
            second = start + 1
            return get_non_repeating_substring(get_string, start, second, size)
    else:
        if get_string[start] == get_string[second]:
            get_string = get_string[:second]
            size = len(get_string)-1
            return get_non_repeating_substring(get_string, start+1, second+1, size)
        else:
            return get_non_repeating_substring(get_string, start, second+1, size)   

get_string = "bbbb"
start = 0
second = 1
size = len(get_string)-1
print(get_non_repeating_substring(get_string, start, second, size))
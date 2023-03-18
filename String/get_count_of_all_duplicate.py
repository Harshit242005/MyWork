#get count of duplicate value
def get_count_duplicate(get_list, start, second, size, count_value):
    if second > size:
        
        if start > size-1:
            return 
        else:
            if count_value > 1:
                print(get_list[start], count_value)  
                start = start+2
                second = start+1
                count_value = 1
                return get_count_duplicate(get_list, start, second, size, count_value)
            else:
                start += 1
                second = start+1
                return get_count_duplicate(get_list, start, second, size, count_value)
    else:
        if get_list[start] == get_list[second]:
          
            return get_count_duplicate(get_list, start, second+1, size, count_value+1)
        else:
            
            return get_count_duplicate(get_list, start, second+1, size, count_value)

get_string = "hllommto"
get_list = list(get_string)
get_list.sort()
start = 0
second = 1
size = len(get_string)-1
count_value = 1
get_count_duplicate(get_list, start, second, size, count_value)
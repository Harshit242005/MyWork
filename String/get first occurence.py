def get_the_first_occurence(start, size, small_string, big_string, length):
    if start > size:
        return 
    else:
        new_string = big_string[start:length+start]
        if new_string == small_string:
            return start
        else:
            start += 1
            return get_the_first_occurence(start, size, small_string, big_string, length)
        
start = 0
small_string = "leeto"
big_string = "leetcode"
size = len(big_string)-1
lenght = len(small_string)
print(f"the string {small_string} occures at {get_the_first_occurence(start, size, small_string, big_string, lenght)}") 
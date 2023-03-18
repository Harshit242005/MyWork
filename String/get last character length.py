def get_last_character_length(get_string):
    words = get_string.split()
    count = 0
    for word in words:
        count += 1
    return len(words[count-1])

get_string = "my name is harshit"
print(f"in the given string the last word has a length of {get_last_character_length(get_string)}")    
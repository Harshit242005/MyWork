def check_anagram(str_1, str_2):
    count_1 = 0
    count_2 = 0
    if len(str_1) == len(str_2):
        for x in range(len(str_1)):
            #print(ord(str_1[x]), end=" ")
            count_1 += ord(str_1[x])
        print()
        for y in range(len(str_2)):
            #print(ord(str_2[y]),end=" ")
            count_2 += ord(str_2[y])

           

        if count_1 == count_2:
            return "it is an anagram"
        else:
            return "it is not an anagram"

    else:
        return "the length of the both the strings are not equal"
str_1 = "aabb"
str_2 = "bbaa"
print(check_anagram(str_1, str_2))                 
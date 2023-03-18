def reverse_sentence(sentence):
    words = sentence.split()
    count = 0
    for word in words:
        count += 1
    i = count-1
    while(i >= 0):
        print(words[i], end=' ')
        i = i - 1

senetence = "my name is harshit"
reverse_sentence(senetence)            
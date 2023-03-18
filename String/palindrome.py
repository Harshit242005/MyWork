class stack:
    def __init__(self):
        self.items = [ ]  # this is the list that i am using to follow up and using 

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    
    def check_palindrome(self, get_string):
        for x in range(len(get_string)):
            self.push(get_string[x])        
        new_string = ""
        # print("the size of the string is : ", self.size())
        print()
        for x in range(0, self.size()):
            new_string += self.pop()
        if get_string == new_string:
            print("the string is a palindrome")
        else:
            print("the string is not a palindrome")       

        

S = stack() 
my_string = input('Enter the string you want to check\t')
S.check_palindrome(str(my_string))
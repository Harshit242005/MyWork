# function to sort the given stack
class Stack:
    def __init__(self):
        self.list_1 = []
        self.list_2 = []

    def push(self, x):
        self.list_1.append(x)

    def pop(self):
        if len(self.list_1) == 0:
            print("stack is empty")
            return 
        else:
            return self.list_1.pop()
        
    def pop_1(self):
        if len(self.list_2) == 0:
            return 
        else:
            return self.list_2.pop()    
        
    def size(self):
        if len(self.list_1) == 0:
            return 0
        else:
            return len(self.list_1)  

    def size_1(self):
        if len(self.list_1) == 0:
            return 0
        else:
            return len(self.list_2)      

    def top(self):
        if len(self.list_1) == 0:
            return 
        else:
            return self.list_1[self.size()-1]
               
    def top_1(self):
        if len(self.list_2) ==0:
            return 
        else:
            return self.list_2[self.size_1()-1]    

    def sort_stack(self):
        if self.size == 0:
            return 
        self.list_2.append(self.pop()) 
        start_element = self.top()
        check_element = self.top_1()
        if check_element < start_element:
            return self.sort_stack()
        else:
            new_element = self.pop_1()
            self.list_1.append(new_element)
            self.list_2.append(start_element)
            return self.sort_stack()
        

    def get_sort_list(self):
        if len(self.list_2) == 0:
            return 
        else:
            print(self.list_2)
            return 
        
if __name__ == "__main__":
    s = Stack()
    s.push(2)
    s.push(1)
    s.push(6)
    s.push(4)
    s.push(5)
    s.sort_stack()
    s.get_sort_list()
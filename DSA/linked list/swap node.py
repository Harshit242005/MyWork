class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return 
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = new_node
            new_node.next = None

    def print_nodes(self):
        if self.head == None:
            return 
        else:
            temp = self.head
            while(temp != None):
                print(temp.data, end=" ")
                temp = temp.next

    def get_length(self):
        if self.head == None:
            return 
        else:
            count = 0
            temp = self.head
            while(temp != None):
                count += 1
                temp = temp.next
            return count                

    def swap_node(self, pos):
        
        if pos == 0 or self.head == None:
            return 
        
        
        
        else:
            count = self.get_length() - pos 
            i = 1
            j = 1
            temp_1 = self.head
            temp_2 = self.head
            while(i <= pos):
                temp_1 = temp_1.next
                i += 1
            print(temp_1.data)
                
            while(j < count):
                temp_2 = temp_2.next
                j += 1
            z = temp_1.data
            temp_1.data = temp_2.data
            temp_2.data = z
            return    
            

if __name__ == "__main__":
    l = Linked_list()
    for x in range(1, 11):
        l.add_node(x)
    l.print_nodes()
    l.swap_node(1)  
    print()
    l.print_nodes()           
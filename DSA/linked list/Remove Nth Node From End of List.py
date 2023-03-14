class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add_node(self, x):
        new_node = Node(x)
        if self.head == None:
            self.head = new_node
            return 
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            current.next = new_node
            new_node.next = None

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
    

    def delete_nth_node(self, pos):
        first = self.head
        if self.head == None or pos == 0:
            return 
        
        if self.head.next == None and pos == 1:
            return None
        
        if pos == self.get_length() - 1:
            self.head = first.next
            return
        else:
            count = self.get_length() - pos 
            temp = self.head
            i = 1
            while(i < count):
                prev = temp
                temp = temp.next
                i += 1
            prev.next = temp.next

            

    def print_nodes(self):
        if self.head is None:
            return 
        else:
            current = self.head
            while(current != None):
                print(current.data, end=" ")
                current = current.next


if __name__ == "__main__":
    l = linked_list()
    for x in range(1, 11):
        l.add_node(x)
    l.print_nodes()       
    print()
    l.delete_nth_node(9)
    l.print_nodes()                               
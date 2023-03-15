class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node_at_end(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = None
            return 
        else:
            self.tail.next = new_node
            new_node.next = None
            self.tail = new_node

    def add_node_at_head(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = None
            return 
        else:
            new_node.next = self.head
            self.head = new_node
            

    def delete_at_end(self):
        temp = self.head
        if self.head is None:
            return 
        else:
            while(temp.next != None):
                prev = temp
                temp = temp.next
            prev.next = None
            self.tail = prev


    def delete_at_head(self):
        temp = self.head
        if self.head is None:
            return 
        else:
            self.head = temp.next


    def print_nodes(self):
        if self.head is None:
            return 
        else:
            temp = self.head
            while(temp != None):
                print(temp.data, end=' ')
                temp = temp.next

if __name__ == "__main__":
    d = deque()
    d.add_node_at_end(1)
    d.add_node_at_end(2)
    d.add_node_at_end(3)
    d.print_nodes()       
    d.add_node_at_head(10)
    d.add_node_at_head(20)
    print()
    d.print_nodes()  
    print()
    d.delete_at_end()
    d.print_nodes()         
    print()
    d.delete_at_head()
    d.print_nodes()                                              
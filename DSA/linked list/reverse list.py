class Node:
    def __init__(self, data):
        # so we have decleared two pointer and see what happens
        self.data = data
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None  

    def add_node(self, x):
        new_node = Node(x)
        if self.head == None:
            self.head = new_node
            self.prev = new_node
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def print_nodes(self):
        if self.head is None:
            return 
        else:
            temp = self.head
            prev_temp = None
            while(temp != None):
                prev_temp = temp
                print(temp.data, end=" ")
                temp = temp.next
            print()    
            print("reverse version of the list")    
            while(prev_temp != None):
                print(prev_temp.data, end=" ")
                prev_temp = prev_temp.prev


if __name__ == "__main__":
    l = doubly_linked_list()
    for x in range(1, 11):
        l.add_node(x)
    l.print_nodes()                                              
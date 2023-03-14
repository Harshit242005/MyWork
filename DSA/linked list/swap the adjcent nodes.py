class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def add_node(self, data):
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

    def print_nodes(self):
        if self.head == None:
            return 
        else:
            temp = self.head
            while(temp != None):
                print(temp.data, end=" ")
                temp = temp.next

    def swap_nodes(self):
        if self.head == None:
            return 
        else:
            temp_1 = self.head
            temp_2 = temp_1.next

            while(temp_2.next != None):
                x = temp_1.data
                temp_1.data = temp_2.data
                temp_2.data = x
                temp_1 = temp_1.next.next
                temp_2 = temp_2.next.next

            y = temp_1.data
            temp_1.data = temp_2.data
            temp_2.data = y    

if __name__ == '__main__':
    l = Linked_list()
    for x in range(1, 11):
        l.add_node(x)
    l.print_nodes() 
    l.swap_nodes()
    print()
    l.print_nodes()
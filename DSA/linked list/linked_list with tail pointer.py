# making the circualr linked list with the pointer 
# by using the tail pointer we can decrease the time complexity of some time consuming opeartions like this
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circualr_list:
    def __init__(self):
        self.head = None
        self.tail = None


    def add_node(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            return 
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
            return 

    def print_nodes(self):
        if self.head is None:
            return 
        else:
            temp = self.head
            print(temp.data, end=' ')
            while(temp.next != self.head):
                temp = temp.next
                print(temp.data, end=" ")
            print()     

    def add_node_at_end(self, value):
        new_node = Node(value)
        if self.head is None:
            return 
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node        

    def add_node_at_head(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
            return 
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.head = new_node   

    def delete_head(self):
        temp = self.head
        if self.head is None:
            return 
        else:
            self.tail.next = self.head.next
            self.head = temp.next


if __name__ == "__main__":
    c = circualr_list()
    for x in range(1, 11):
        c.add_node(x)
    c.print_nodes()                
    c.add_node_at_end(100)
    c.print_nodes()
    c.add_node_at_head(200)
    c.print_nodes()
    c.delete_head()
    c.print_nodes()
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None
        self.prev = None

class doubly_linked_list:
    def __init__(self):
        self.head = None


    def add_node(self, x):
        new_node = Node(x) 
        if self.head is None:
            self.head = new_node
            return
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
            new_node.next = None

    def add_node_at_head(self, x):
        new_node = Node(x)
        temp = self.head
        if self.head is None:
            self.head = new_node
            return 
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def add_node_at_middle(self, value, pos):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return 
        else:
            i = 1
            temp = self.head
            while(i <= pos):
                prev_node = temp
                temp = temp.next
                i += 1
            prev_node.next = new_node
            new_node.next = temp.next
            new_node.prev = prev_node
            temp.prev = new_node  


    def add_node_at_last(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            return 
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def delete_head(self):
        if self.head is None:
            return
        else:
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            return         
             

    def print_node(self, head):
        if head is None:
            return 
        else:
            while(head != None):
                prev_node = head
                print(head.data, end=" ")
                head = head.next            
            print()
            while(prev_node != None):
                print(prev_node.data, end=" ")
                prev_node = prev_node.prev


    def delete_last(self):
        if self.head is None:
            return 
        else:
            temp = self.head
            while(temp.next != None):
                prev_node = temp
                temp = temp.next
            prev_node.next = None        

    def delete_middle(self, pos):
        if self.head is None:
            return 
        else:
            i = 1
            temp = self.head
            while(i <= pos-1 and temp.next != None):
                prev_node = temp
                temp = temp.next
                i += 1
            prev_node.next = temp.next
            temp.next.prev = prev_node
            

if __name__ == "__main__":
    l = doubly_linked_list()
    for x in range(1, 11):
        l.add_node(x)  
    l.print_node(l.head)       
    
# using all the formulas in the circular linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class circular_linked_list:
    def __init__(self):
        self.head = None

    def add_node(self, x):
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return 
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
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

    def check_circular(self):
        if self.head is None:
            return 
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            if temp.next == self.head:
                return "this is a circualr linked list"
            else:
                return "this is not a circular linked list"   
    # this will add the node by trnasversing the whole linked list like and hae a time complexity of O(n)         
    def add_node_at_head(self, x):
        temp = self.head
        new_node = Node(x)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return 
        else:
            while(temp.next != self.head):
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head
            self.head = new_node    

    def add_node_anywhere(self, value, pos):
        if self.head is None:
            return 
        if pos < 1:
            return 
        if pos == 1:
            return c.add_node_at_head(value)
        new_node = Node(value)
        temp = self.head
        i = 1
        while(i <= pos-1 and temp is not None):
            prev = temp
            temp = temp.next
            i += 1
        prev.next = new_node
        new_node.next = temp.next
        return     

    def delete_head(self):
        temp = self.head
        if self.head is None:
            return 
        else:
            self.head = temp.next
            while(temp.next.next != self.head):
                temp = temp.next
            temp.next = self.head
            return 

    def delete_last(self):
        if self.head is None:
            return 
        else:
            temp = self.head
            while(temp.next != self.head):
                prev = temp
                temp = temp.next
            prev.next= self.head
            return    
        
    # this will delete node at anywhere
    def delete_anywhere(self, pos):
        if self.head is None:
            return 
        if pos < 1:
            return      
        if pos == 1:
            return self.delete_head()
        else:
            temp = self.head
            i = 1
            while(i <= pos-1 and temp.next != None):
                prev = temp
                temp = temp.next    
                i += 1 
            prev.next = temp.next
            return      

    # this will make the print function fail as they try to make the circualr list singley
    def make_singly(self):
        if self.head is None:
            return 
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = None
            return       

    def check_if_node_exist(self, value):
        if self.head is None:
            return 
        else:
            temp = self.head
            while(temp.next != self.head):
                if temp.data == value:
                    return "node exits"
                temp = temp.next
            return "node does not exist"

if __name__ == "__main__":
    c = circular_linked_list()
    for x in range(1, 11):
        c.add_node(x)
    c.print_nodes()       
    print()
    c.add_node_at_head(100)
    c.add_node_at_head(200)
    c.add_node_anywhere(500, 3)
    c.print_nodes()            
    c.delete_head()
    c.print_nodes()   
    c.delete_last()
    c.print_nodes()         
    print()
    c.delete_anywhere(3)
    c.print_nodes()   
    print()
    print(c.check_if_node_exist(5))
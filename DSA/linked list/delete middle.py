class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
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
            new_node.next = None
            return 

    def print_node(self, head):
        if head is None:
            return 
        else:
            while(head != None):
                print(head.data, end=" ")
                head = head.next
              
            

    def get_lenght(self, head):
        if head is None:
            return 0 
        else:
            count = 1
            while(head != None):
                count += 1
                head = head.next
            return count            

    

    
    def delete_middle(self, head):
        if self.head is None:
            return 
        else:
            lenght = self.get_lenght(head) // 2
            i = 1
            while(i < lenght):
                prev = head
                head = head.next
                i += 1
            prev.next = head.next
            return         
            
    
if __name__ == "__main__":
    l = linked_list()
    for x in range(1, 11):
        l.add_node(x)
    l.print_node(l.head)
    print()
    l.delete_middle(l.head)
    print()
    l.print_node(l.head)
    
    print(f"the length of the llist is {l.get_lenght(l.head)}")
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
                

    def sort_list(self, start, second):
        if second is None:
            if start.next is None:
                return 
            else:
                start = start.next
                second = start.next
                return self.sort_list(start, second)  

        else:
            if start.data < second.data:
                return self.sort_list(start, second.next)
            else:
                x = start.data
                start.data = second.data
                second.data = x
                return self.sort_list(start, second.next)              
            
    
if __name__ == "__main__":
    l = linked_list()
    l.add_node(2)
    l.add_node(3)
    l.add_node(1)
    l.add_node(8)
    l.add_node(7)
    l.print_node(l.head)
    print()     
    x = l.head
    y = x.next          
    l.sort_list(x, y)
    l.print_node(l.head)   
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linekd_list:
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

    def print_nodes(self, head):
        if self.head is None:
            return 
        else:
            
            while(head != None):
                print(head.data, end=" ")
                head = head.next


    def add_numbers(self, head_1, head_2):
        x = None
        if head_1 and head_2 is None:
            return 
        if head_1 is None:
            return self.print_nodes(head_2)
        if head_2 is None:
            return self.print_nodes(head_1)      

        else:
            if head_1.data + head_2.data > 10:
                x = (head_1.data + head_2.data) % 10
                return self.add_numbers(head_1.next, head_2.next)
                print(x, end=" ")
            if head_1.data + head_2.data < 10:
                print(head_2.data + head_1.data, end=" ")
                return self.add_numbers(head_1.next, head_2.next)
            if head_1.data + head_2.data == 10:
                print(0, end=" ")
                head_1.next.data = head_1.next.data + 1
                return self.add_numbers(head_1.next, head_2.next)  

if __name__ == "__main__":
    l1 = Linekd_list()
    l2 = Linekd_list()                     
    for x in range(1, 4):
        l1.add_node(x)
    for y in range(4, 7):
        l2.add_node(y)

    l1.print_nodes(l1.head)
    print()
    l2.print_nodes(l2.head)
    print()
    l1.add_numbers(l1.head, l2.head)
    

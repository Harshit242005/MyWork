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


    def print_nodes(self, head):
        if self.head is None:
            return 
        else:
            while(head != None):
              print(head.data, end=" ")
              head = head.next  


    def merge_sort_list(self, head_1, head_2):
        if head_1 is None:
            return self.print_nodes(head_2)
        if head_2 is None:
            return self.print_nodes(head_1)
        else:
            if head_1.data > head_2.data:
                print(head_2.data, end=" ")
                return self.merge_sort_list(head_1, head_2.next)
            if head_1.data < head_2.data:
                print(head_1.data, end=" ")
                return self.merge_sort_list(head_1.next, head_2)
            if head_1.next is None:
                return self.print_nodes(head_2)
            if head_2.next is None:
                return self.print_nodes(head_1) 

l_1 = linked_list()
l_2 = linked_list()
for x in range(1, 4):
    l_1.add_node(x)
for y in range(4, 7):
    l_2.add_node(y)
l_1.print_nodes(l_1.head)
print() 
l_2.print_nodes(l_2.head)
print()
l_1.merge_sort_list(l_1.head, l_2.head)  
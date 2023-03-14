class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = None

    def add_node(self, x):
        new_node = Node(x)
        if self.head == None:
            self.head = new_node
            return 
        else:
            temp = self.head
            while(temp.next != None):
                temp = temp.next
            temp.next = new_node
            new_node.next = None

    def print_nodes(self):
        if self.head is None:
            return 
        else:
            temp = self.head
            while(temp is not None):
                print(temp.data, end=" ")
                temp = temp.next

    def get_length(self):
        if self.head is None:
            return 
        else:
            count = 0
            temp = self.head
            while(temp is not None):
                count += 1
                temp = temp.next 
            return count                

    def delete_node(self, pos):
        if self.head is None or pos > self.get_length():
            return 
        else:
            i = 1
            temp = self.head
            while(i <= pos):
                prev = temp
                temp = temp.next
                i += 1
            if temp.next != None:
                prev.next = temp.next
            else:
                prev.next = None

    def get_duplicate_delete(self, start, second, pos):
        if second is None:
            if start.next is None:
                return 
            else:
                start = start.next
                second = start.next
                pos = 2
                return self.get_duplicate_delete(start, second, pos)
        else:
            if start.data == second.data:
                self.delete_node(pos)
                return self.get_duplicate_delete(start, second.next, pos+1)
            else:
                return self.get_duplicate_delete(start, second.next, pos+1)
            
if __name__ == '__main__':
    l = linked_list()
    l.add_node(1)
    l.add_node(2)
    l.add_node(1)
    l.add_node(3)
    l.add_node(2)
    l.add_node(4)
    l.add_node(5)            
    l.print_nodes()
    print()
    x = l.head
    y = x.next
    pos = 1
    l.get_duplicate_delete(x, y, pos)
    l.print_nodes()
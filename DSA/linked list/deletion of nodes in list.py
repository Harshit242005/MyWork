class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
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

    def delete_with_pos(self, pos):
        temp = self.head
        if self.head == None:
            return 
        if pos == 1:
            self.head = temp.next
        else:
            i = 1
            while(i <= pos-1):
                prev = temp
                temp = temp.next
                i += 1
            prev.next = temp.next 

    def delete_data_points(self, value):
        temp = self.head
        if self.head == None:
            return 
        if self.head.data == value:
            self.head = temp.next
        while(temp.data != value):
            prev = temp
            temp = temp.next
        prev.next = temp.next  

    def delete_all_nodes(self, start, value):
        
        if self.head is None or start is None:
            return 
        if start.data == value:
            self.delete_data_points(value)
            return l.delete_all_nodes(start.next, value)
        else:
            return l.delete_all_nodes(start.next, value)

if __name__ == "__main__":
    l = Linked_list()
    arr = [1, 2, 4, 2, 4, 5, 7]
    for x in range(len(arr)):
        l.add_node(arr[x])
    l.print_nodes()  
    x = l.head     
    l.delete_all_nodes(x, 1)
    print()
    l.print_nodes()        
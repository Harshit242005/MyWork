class Node:
    def __init__(self, data):
        self.data = data
        self.next =  None

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
            while(temp != None):
                print(temp.data, end=" ")
                temp = temp.next

    def make_cycle(self):
        temp = self.head
        if self.head is None:
            return 
        else:
            while(temp.next != None):
                temp = temp.next
            temp.next = self.head

    def has_cycle(self, head):
    # Initialize the slow and fast pointers
        slow = head
        fast = head
    
    # Traverse the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Check if the fast pointer has caught up to the slow pointer
            if slow == fast:
                return True
    
    # If the fast pointer reaches the end of the list, there is no cycle
        return False


if __name__ == "__main__":
    l = linked_list()
    for x in range(1, 11):
        l.add_node(x)
    l.print_nodes()
    print()
    l.make_cycle()    
    print()
    if(l.has_cycle(l.head)):
        print("list has the cycle")
    else:
        print("list does not have a cycle")  
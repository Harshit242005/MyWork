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
                

    # def sort_list(self, start, second):
    #     if second is None:
    #         if start.next is None:
    #             return 
    #         else:
    #             start = start.next
    #             second = start.next
    #             return self.sort_list(start, second)  

    #     else:
    #         if start.data < second.data:
    #             return self.sort_list(start, second.next)
    #         else:
    #             x = start.data
    #             start.data = second.data
    #             second.data = x
    #             return self.sort_list(start, second.next)  
            

    def get_lenght(self, head):
        if head is None:
            return 0 
        else:
            count = 0
            while(head != None):
                count += 1
                head = head.next
            return count            

    def part_the_list(self, start, target):
        if start is None or target < 1:
            return 
        if self.get_lenght(start) < target:
            return self.print_node(start)
        else:
            i = 0
            while(i < target):
                print(start.data)
                start = start.next
                i += 1
            print()
            next_start = start
            return self.part_the_list(next_start, target)
            
    
if __name__ == "__main__":
    l = linked_list()
    for x in range(1, 11):
        l.add_node(x)
    l.print_node(l.head)
    print()
    l.part_the_list(l.head, 3)
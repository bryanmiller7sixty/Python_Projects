class Node:
    def __init__(self, data=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def add(self, data):
        print("Adding ", data)
        current = self.head
        prev = self.head
        if current == None:
            self.head = Node(data)
        else:
            while(current.next):
                current = current.next
            current.next = Node(data)
    def display(self):
        str = "[ "
        current = self.head
        while(current):
            str += f'{current.data} '
            current = current.next
        str+="]"
        print(str)
    def reversed(self):
        current = self.head
        prev = None;
        following = self.head
        while (current):
            following = following.next
            current.next = prev
            prev = current
            current = following
        self.head = prev
llist = LinkedList()
llist.add(1)
llist.add(2)
llist.display()



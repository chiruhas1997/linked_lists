

class Node:
    def __init__(self,data = None, next = None, previous = None):
        self.data = data
        self.next = next
        self.previous = previous

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_start(self,data):
        if self.head == None:
            self.head(data, None, None)
            return 
        self.head = Node(data, self.head, None)
        self.head.next.previous = self.head

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None, None)
            self.tail = self.head
            return
        
        self.tail.next = Node(data, None, self.tail)
        self.tail = self.tail.next

    def print_from_front(self):

        itr = self.head
        ls = ''
        while itr:
            ls +=str(itr.data)+'-->'
            itr = itr.next
        print(ls)

    def print_from_back(self):
        itr = self.tail
        ls = ''

        while itr:
            ls +=str(itr.data)+'-->'
            itr = itr.previous
        print(ls)

    def insert_list(self, num_list):
        self.head = None
        self.tail = None
        
        for n in num_list:
            self.insert_at_end(n)

llist = LinkedList()
# llist.insert_at_end(5)
# llist.insert_at_end(10)
# llist.insert_at_end(15)
# llist.insert_at_start(0)
llist.insert_list([0,1,2,3,4,5])
llist.print_from_front()
llist.print_from_back()
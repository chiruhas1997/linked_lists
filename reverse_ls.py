

class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return 
        
        itr = self.head
        while(itr.next):
            itr = itr.next
        itr.next = Node(data,None)

    def insert_list(self,list_data):
        self.head = None

        for n in list_data:
            self.insert_at_end(n)

    def print(self):
        if self.head is None:
            print("empty linked list")
            return
        itr = self.head
        lis = ''
        while itr:
            lis += str(itr.data) + '-->'
            itr = itr.next
        print(lis)    

    def reverse(self):

        previous = None
        itr = self.head
        current = self.head

        while itr:
            itr = itr.next

            current.next = previous
            previous = current
            current = itr
        self.head = previous


if __name__ == "__main__":

    llist = LinkedList()
    llist.insert_list([1,2,3,4,5,6])
    llist.print()
    llist.reverse()
    llist.print()
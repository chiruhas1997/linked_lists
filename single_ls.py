

class Node:
    def __init__(self,data = None,next = None):
        self.data = data
        self.next = next

class LinkedLisr:
    def __init__(self):
        self.head = None
    
    def insert_at_start(self,data):
        node = Node(data,self.head)
        self.head = node

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

    def length(self):
        length = 0
        itr = self.head
        while itr:
            length+=1
            itr = itr.next
        return length

    def delete_at(self,index):
        if index<0 or index>=self.length():
            raise Exception("invalid index")
        
        if index == 0:
            self.head = self.next
            return
        
        current = 0
        itr = self.head
        while itr:

            if current == index-1:
                itr.next = itr.next.next
                return
            itr = itr.next
            current += 1
        

    def insert_at(self,index,data):
        if index<0 or index>self.length():
            raise Exception("invalid index")

        if index == 0:
            self.head = Node(data,self.head)
            return

        current = 0
        itr = self.head
        while itr:

            if current == index-1:
                node = Node(data, itr.next)
                itr.next = node
                return
            itr = itr.next
            current+=1

    def insert_before_value(self,data,value):

        if self.head.data == value:
            self.insert_at_start(data)
            return
            
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                node = Node(data, itr.next)
                itr.next = node
                return
            itr = itr.next


    def delete_by_value(self,value):

        if value == self.head.data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                return
            itr = itr.next

llist = LinkedLisr()
llist.insert_list([1,2,3,4,5,6])
llist.print()
llist.delete_by_value(0)
llist.print()







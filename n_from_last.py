from return_head import LinkedList

def getNode(llist, positionFromTail):
    
    fast_point = llist
    slow_point = llist
    
    for _ in range(positionFromTail):
        fast_point=fast_point.next
    while fast_point:
        fast_point=fast_point.next
        slow_point=slow_point.next
    return slow_point.data


ll = LinkedList()
ll.insert_list([1,2,5,7,4])
ll.print()
print(getNode(ll.return_head(),5))
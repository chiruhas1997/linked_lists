from return_head import LinkedList

def mergr_ll(head1,head2):

    if head1 == None and head2 == None:
        return None
    if head1 == None:
        return head2
    if head2 == None:
        return head1

    if head1.data < head2.data:
        temp = head1
        temp.next = mergr_ll(head1.next,head2)
    else:
        temp = head2
        temp.next = mergr_ll(head1, head2.next)
    
    return temp 

ll1 = LinkedList()
ll1.insert_list([4,5,8,12,46])
head1 = ll1.return_head()

ll2 = LinkedList()
ll2.insert_list([1,3,5,11])
head2 = ll2.return_head()


temp = mergr_ll(head1, head2)
lis=''
while temp:
    lis += str(temp.data) + '-->'
    temp = temp.next
print(lis)

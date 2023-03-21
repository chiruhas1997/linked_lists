#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def list_length(head):
    count=0
    while head:
        count+=1
        head=head.next
    return count

def getMerge(d, head1, head2):
    for _ in range(d):
        head1=head1.next
    while head1:
        if head1==head2:
            return head1.data
        head1=head1.next
        head2=head2.next

def findMergeNode(head1, head2):
    count1 = list_length(head1)
    count2 = list_length(head2)
    
    if count1>count2:
        value = getMerge(count1-count2,head1,head2)
    else:
        value = getMerge(count2-count1,head2,head1)
    return value
if __name__ == '__main__':
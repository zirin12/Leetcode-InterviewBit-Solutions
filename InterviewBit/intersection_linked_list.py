'''

Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3

begin to intersect at node c1.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
 
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    
    # Traverse with 2 pointers till the common end and find out the difference between the lengths of non overlapping  lists
    # use this difference to to start traversing the smaller list as soon as the count hits diff when traversing the longer
    # list . The two pointers will then eventually meet where they overlap , check for this and return the common node.
    def getIntersectionNode(self, A, B):
        if A is B :
            return A
        l1 = A
        l2 = B
        dist = 0
        flag = True
        while l1 and l2:
            if l1 is l2 :
                return l1
            l1 = l1.next
            l2 = l2.next
            
        if l1:
            while l1:
                l1 = l1.next
                dist += 1
        elif l2:
            flag = False
            while l2:
                l2 = l2.next
                dist+=1
        else:
            return None
            
        l1 = A
        l2 = B
        if not flag:
            l1 = B
            l2 = A
        count = 0
        while l1 and l2 :
            if l1 is l2 :
                return l1
            l1 = l1.next
            if count >= dist :
                l2 = l2.next
            count += 1
        return None

'''
  Reverse a linked list using recursion.
'''

# Definition for singly-linked list.
# class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    
    # one of way doing it without passing head node as parameter
    # iterate each time to the end 
    def reverseList(self, A):
        if A.next == None :
            return A
        L = self.reverseList(A.next)
        B = L
        while B.next:
            B = B.next
        B.next = A
        A.next = None
        return L

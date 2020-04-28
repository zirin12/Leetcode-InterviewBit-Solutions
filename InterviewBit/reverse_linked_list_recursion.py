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
    def reverseList_1(self, A):
        if A.next == None :
            return A
        L = self.reverseList(A.next)
        B = L
        while B.next:
            B = B.next
        B.next = A
        A.next = None
        return L
    
    # Set temp to next node , reverse the list from the next node
    # set temp.next to A , so that it will be added at the end of list
    def reverseList_2(self, A):
        if A.next == None :
            return A
        temp = A.next
        L = self.reverseList(A.next)
        A.next = None
        temp.next = A
        return L

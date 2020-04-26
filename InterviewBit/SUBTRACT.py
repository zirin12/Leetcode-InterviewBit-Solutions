'''
  Given a singly linked list, modify the value of first half nodes such that :

    1st node’s new value = the last node’s value - first node’s current value
    2nd node’s new value = the second last node’s value - 2nd node’s current value,

    and so on …

    Example :

    Given linked list 1 -> 2 -> 3 -> 4 -> 5,

    You should return 4 -> 2 -> 3 -> 4 -> 5
'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    
    # Reverse the 2nd part of linked list , do the required operation , reverse it back again to orginal
    # Improvement : Make a function for reversing and call it rather than writing it every time
    # Improvement : Reverse the 1st part of linked list , it will make things easier
    def subtract(self, A):
        n = 0 
        L = A
        while L :
            n += 1
            L = L.next
        if n == 1:
            return A
            
        if n == 2:
            A.val = A.next.val - A.val
            return A
        
        # Get the 2nd half of the linked list
        count = 0
        M = A
        prev = None
        while count != (n//2):
            prev = M
            M = M.next
            count += 1
            
        # reverse the 2nd part of linked list
        p_node = None
        c_node = M if n%2==0 else M.next
        while c_node :
            n_node = c_node.next
            c_node.next = p_node
            p_node = c_node
            c_node = n_node
        
        # set ending of 1st part to null otherwise will later lead to cycle
        if n%2 == 0:
            prev.next = None
        else :
            prev.next.next = None
        
        # Do the required operation for the corresponding elements
        B = A
        p_node_copy = p_node
        while p_node_copy.next :
            B.val = p_node_copy.val - B.val
            B = B.next
            p_node_copy = p_node_copy.next
        
        # last node of the 1st part of linked list if length is even
        # last but one if odd
        B.val = p_node_copy.val - B.val
        
        # reverse back the 2nd part of list to restore back original linked list
        p_node_new = None
        c_node = p_node
        while c_node :
            n_node = c_node.next
            c_node.next = p_node_new
            p_node_new = c_node
            c_node = n_node
            
        # take care of even and odd case
        if n%2 ==0 :
            B.next = p_node_new
        else :
            B.next.next = p_node_new
        return A

'''
  Given a singly linked list, determine if its a palindrome. 
  Return 1 or 0 denoting if its a palindrome or not, respectively.
'''


# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return an integer
  
  # Find the length of list
  # use logic from reverse the linked list
  # Reverse till the list till the middle and then keep comparing the reversed list and the rest of the list.
	def lPalin(self, A):
	    Len = 0
	    l1 = A
	    while l1:
	        Len += 1
	        l1 = l1.next
        
        count = 0
        odd = (Len%2!=0)
        p_node = None
        c_node = A
        n_node = None
        while count < (Len//2) :
            n_node = c_node.next
            c_node.next = p_node
            p_node = c_node
            c_node = n_node
            count += 1
            
        c_node = c_node.next if odd else c_node
        
        while c_node:
            if c_node.val != p_node.val:
                return 0
            c_node = c_node.next
            p_node = p_node.next
        return 1
            

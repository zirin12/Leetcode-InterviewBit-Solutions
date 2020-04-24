'''
  Reverse a linked list. Do it in-place and in one-pass.
'''

# Definition for singly-linked list.
# class ListNode:
#	def __init__(self, x):
#		self.val = x
#		self.next = None

class Solution:
	# @param A : head node of linked list
	# @return the head node in the linked list
  
  # Iterative approach
  # Use 3 variables previous ,current and next to manipluate , set initially previous to None and current to head
  # In while keep manipulating these 3 variables till current is None , Then return the previous node
  def reverseList(self, A):
      p_node = None
      c_node = A
      while c_node:
        n_node = c_node.next
        c_node.next = p_node
        p_node = c_node
        c_node = n_node
      return p_node
	    

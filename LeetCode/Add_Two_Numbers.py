# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class Solution:
    def addTwoNumbers_1(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = ""
        num2 = ""
        while(l1!=None) :
            num1+=str(l1.val)
            l1 = l1.next
            
        while(l2!=None):
            num2+=str(l2.val)
            l2 = l2.next
            
        num3 = str(int(num1[::-1]) + int(num2[::-1]))[::-1]
        
            
        head = ListNode(0)
        start = head
        for char in num3:
            start.next = ListNode(int(char))
            start = start.next
            
        return head.next
   
        
    
    def addTwoNumbers_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        start = head
        carry=0
        while l1 or l2 or carry:
            num1 = (l1.val if l1 else 0)
            num2 = (l2.val if l2 else 0)
            carry,num = divmod(num1+num2+carry,10)
            start.next = ListNode(num)
            start = start.next
            l1=(l1.next if l1 else 0)
            l2=(l2.next if l2 else 0)
            
        return head.next

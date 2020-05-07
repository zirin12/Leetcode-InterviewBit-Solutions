'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

    1.The left subtree of a node contains only nodes with keys less than the node’s key.
    2.The right subtree of a node contains only nodes with keys greater than the node’s key.
    3.Both the left and right subtrees must also be binary search trees.

'''

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    
    # Tried the naive approach first where we check recursively if each left and right node is a binary search tree
    # Naive method doesn't work because there can be element in the left or right subtree that can be greater or less than the
    # parent itself. 
    # So we need to check if the largest element in the left subtree and smallest element in right subtree obey the rules . 
    # largest element in the left subtree and smallest element in right subtree can again be found using recursion 
    
    # Another method could be to get the inorder traversal and see if it's sorted or not as inorder traversal represents the 
    # sorted order of a BST
    
    def largest_left_subtree(self, A):
        if A is None :
            return None
        if A.left is None and A.right is None :
            return A.val
        r = A.right
        if r is None:
            return A.val
        return self.largest_left_subtree(r)
            
    def smallest_right_subtree(self, A):
        if A is None :
            return None
        if A.left is None and A.right is None :
            return A.val
        l = A.left
        if l is None:
            return A.val
        return self.smallest_right_subtree(l)
    
    def isValidBST(self, A):
        if A is None :
            return 1
        if self.isValidBST(A.left) and self.isValidBST(A.right):
            l = A.left.val < A.val if A.left else True
            r = A.right.val > A.val if A.right else True
            if l==False or r==False :
                return 0
            left = self.largest_left_subtree(A.left)
            right = self.smallest_right_subtree(A.right)
            if (left and left >= A.val) or (right and right <= A.val):
                return 0
            return 1
        return 0
        
***************************************************************************************************************************

# Simplified implementation of the above

# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    
    # Don't check for the traditional BST check as in if the left node is smaller and right node is bigger than the
    # parent node
    # Remove those conditions and simplify the recursion
    # This will check if all the nodes are in order or not.
    def largest_left_subtree(self, A):
        if A is None :
            return None
        if A.right is None:
            return A.val
        return self.largest_left_subtree(A.right)
            
    def smallest_right_subtree(self, A):
        if A is None :
            return None
        if A.left is None:
            return A.val
        return self.smallest_right_subtree(A.left)
    
    def isValidBST(self, A):
        if A is None :
            return 1
        if self.isValidBST(A.left) and self.isValidBST(A.right):
            left = self.largest_left_subtree(A.left)
            right = self.smallest_right_subtree(A.right)
            if (left and left >= A.val) or (right and right <= A.val):
                return 0
            return 1
        return 0
 

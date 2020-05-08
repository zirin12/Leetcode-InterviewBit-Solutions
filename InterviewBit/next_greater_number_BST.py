'''
Given a BST node, return the node which has value just greater than the given node.
Example:

Given the tree

               100
              /   \
            98    102
           /  \
         96    99
          \
           97

Given 97, you should return the node corresponding to 98 as thats the value just greater than 97 in the tree.
If there are no successor in the tree ( the value is the largest in the tree, return NULL).

Using recursion is not allowed.

Assume that the value is always present in the tree.
'''

# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Traverse the tree through iteration till you find the given node .
    # While traversing keep track of the node with the closest greater value , see if the difference is minimum 
    # After the node is found , if it doesn't have a right subtree return the min node from before
    # If  it does have a right subtree , find the smallest value in the right subtree by just traversing to the extreme left
    # return the leftmost node
    
    # @param A : root node of tree
    # @param B : integer
    # @return the root node in the tree
    def getSuccessor(self, A, B):
        l = A
        min_node = None
        while True :
            if B == l.val :
                break
            if B < l.val :
                if (min_node is None) or ((l.val - B) < (min_node.val - B)) :
                    min_node = l
                l = l.left
            else :
                l = l.right
    
        if l.right is None :
            return min_node
        
        temp = l.right
        while temp.left :
            temp = temp.left
        return temp

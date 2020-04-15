'''
**********
INCOMPLETE
**********

Find the kth smallest element in an unsorted array of non-negative integers.
You are not allowed to modify the array ( The array is read only ).
Try to do it using constant extra space.
'''

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    
    # Sort of a hack or cheat , sort and then return element
    # Not recommended at all
    # O(nlogn) as default method is quicksort
    def kthsmallest(self, A, B):
       C = list(A)
       C.sort()
       return C[B-1]
       
    # Solution using binary search ,calculate min and max and then do binary search
    # after finding mid , get occurence of elements lesser than k , also account for elements equal to mid
    def kthsmallest(self, A, B):
    
    
    # Solution using heap , implement the heap and do it
    # later use inbuilt heapq function
    def kthsmallest(self, A, B):
    

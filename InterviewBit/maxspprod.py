'''
You are given an array A containing N integers. The special product of each ith integer in this array is defined as the product of the following:<ul>

LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j). If multiple A[j]’s are present in multiple positions, the LeftSpecialValue is the maximum value of j.

RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i). If multiple A[j]s are present in multiple positions, the RightSpecialValue is the minimum value of j.

Write a program to find the maximum special product of any integer in the array.

Input: You will receive array of integers as argument to function.

Return: Maximum special product of any integer in the array modulo 1000000007.

Note: If j does not exist, the LeftSpecialValue and RightSpecialValue are considered to be 0.
'''

class Solution:
    # @param A : list of integers
    # @return an integer
    
    # Brute force will take too long for large inputs
    # left special index can be computed by comparing left special values starting from the previous element recursively
    # same method for right special value
    # after they are calculated separately find the max product of the indexes.
    def R_find_largest(self,A,i,num,R,n):
        index = i
        while index>0 and index<n:
            index = R[index]
            if A[index] > num:
                return index
        return 0
    
    def L_find_largest(self,A,i,num,L):
        index = i
        while index>0:
            index = L[index]
            if A[index] > num:
                return index 
        return 0
        
    def leftSpecialValue(self, A, n, L):
        L[1] = 0
        for i in range(2,n):
            if A[i-1] > A[i]:
                L[i] = i-1
            elif L[i-1] == 0:
                L[i] = 0
            else:
                L[i] = self.L_find_largest(A,i-1,A[i],L)
                
    def rightSpecialValue(self, A, n, R):
        for i in range(n-2,1,-1):
            if A[i+1] > A[i]:
                R[i] = i+1
            elif R[i+1] == 0 or R[i+1] == -1:
                R[i] = 0
            else :
                R[i] = self.R_find_largest(A,i+1,A[i],R,n)
    
    def maxSpecialProduct(self, A):
        n = len(A)
        if(n<=3):
            return 0
        max_prod = 0
        L = [-1]*n
        R = [-1]*n
        self.leftSpecialValue(A, n, L)
        self.rightSpecialValue(A, n, R)
        for i in range(2,n):
            l = L[i]
            r = R[i]
            max_prod = max((l*r),max_prod)
        return max_prod%1000000007

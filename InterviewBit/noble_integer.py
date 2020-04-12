'''
Given an integer array, find if an integer p exists in the array such that the number of integers greater than p in the array equals to p
If such an integer is found return 1 else return -1.
'''
class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort()
        length = len(A)
        for i in range(0,length):
            if i<length-1 and A[i] == A[i+1]:
                continue
            if A[i]==(length-1-i):
                return 1
        return -1

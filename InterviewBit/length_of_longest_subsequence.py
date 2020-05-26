'''
Given an array of integers, A of length N, find the length of longest subsequence which is first increasing then decreasing.

Input Format:
The first and the only argument contains an integer array, A.

Output Format:
Return an integer representing the answer as described in the problem statement.

Constraints:
1 <= N <= 3000
1 <= A[i] <= 1e7

Example:
Input 1:
    A = [1, 2, 1]
Output 1:
    3
Explanation 1:
    [1, 2, 1] is the longest subsequence.

Input 2:
    [1, 11, 2, 10, 4, 5, 2, 1]
Output 2:
    6    
Explanation 2:
    [1 2 10 4 2 1] is the longest subsequence.
'''

class Solution:
    # @param A : tuple of integers
    # @return an integer
    
    # First compute LIS where each index is where the subsequence will end instead of the longest subsequence fof the whole list
    # Compute LDS where each index is where the decreasing subsequence starts from ( LIS from right to left )
    # With the above two results compare the corresponding values to see which pair has the max sum which will be the max length  
    # Output the result subtracting 1 to account for the repetetion of the middle element. 
    def longestSubsequenceLength(self, A):
        if len(A) == 0:
            return 0
        L = [1]*len(A)
        for i in range(1,len(A)):
            index = i-1
            max_len = 0
            while index >= 0 :
                if A[index] < A[i]:
                    max_len = max(max_len,L[index])
                index -= 1
            L[i] = 1 + max_len if max_len > 0 else 1
            
        R = [1]*len(A)
        for i in range(len(A)-2,-1,-1):
            index = i+1
            max_len = 0
            while index < len(A) :
                if A[index] < A[i]:
                    max_len = max(max_len,R[index])
                index += 1
            R[i] = 1 + max_len if max_len > 0 else 1
     
        diff = 0
        for i in range(len(A)):
            if L[i] + R[i] > diff :
                diff = L[i] + R[i]
                index = i
        return diff - 1

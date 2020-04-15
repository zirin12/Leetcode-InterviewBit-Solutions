class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    
    # This is an O(n^2) method where we calculate sum of all subsequences but break when it's higher than C
    def numRange(self, A, B, C):
        n = len(A)
        seq = 0
        for i in range(n):
            for j in range(i,n):
                S = sum(A[i:j+1])
                if S > C :
                    break
                if B <= S <= C:
                    seq += 1;
        return seq
        
        
    # To do : To get O(n) use Prefix sum and then two pointers one for B and one for C for calculating subarrays less than them respectively
    # Then subtract both the results . 

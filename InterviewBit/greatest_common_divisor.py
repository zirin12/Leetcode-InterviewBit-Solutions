'''
Compute greatest common divisor
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    
    # use euclidean algorithm
    # read extended euclidean algorithm for more info https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/
    def gcd(self, A, B):
        if not A or not B :
            return (A if not B else B) 
        while A>0:
            if B > A:
                A,B = B,A
            if A%B == 0 :
                return B
            A,B = B, A%B
        return B
        
            

'''
Given a column title as appears in an Excel sheet, return its corresponding column number.
'''

class Solution:
    # @param A : string
    # @return an integer
    
    # base is 26 so convert using standard way to decimal
    def titleToNumber(self, A):
        n = len(A)
        num = 0
        for i in range(0,n):
            num += (ord(A[i])-64)*pow(26,n-1-i)
        return int(num)


'''
Print concentric rectangular pattern in a 2d matrix.
Let us show you some examples to clarify what we mean.

Example 1:

Input: A = 4.
Output:

4 4 4 4 4 4 4 
4 3 3 3 3 3 4 
4 3 2 2 2 3 4 
4 3 2 1 2 3 4 
4 3 2 2 2 3 4 
4 3 3 3 3 3 4 
4 4 4 4 4 4 4 


'''


class Solution:
    # @param A : integer
    # @return a list of list of integers
    
    # find the pattern and do it row by row
    def prettyPrint(self, A):
        r = 2*A-1
        result = []
        row = [A]*r
        result.append(row)
        
        for i in range(1,A):
            row = row[:]
            for j in range(i,r-i):
                row[j] = row[j]-1
            result.append(row)
        
        for j in range(A,1,-1):
            row = row[:]
            for i in range(j-1,r-j+1):
                row[i] = row[i] + 1 
            result.append(row)
        return result

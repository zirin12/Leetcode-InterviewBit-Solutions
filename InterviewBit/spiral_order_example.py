'''
Given a matrix of m * n elements (m rows, n columns), return all elements of the matrix in spiral order.
'''
class Solution:
	# @param A : tuple of list of integers
	# @return a list of integers
	def spiralOrder(self, A):
	    m = len(A)
	    n = len(A[0])
	    total = m*n
	    count = 0 
	    direction = [0,0,0,0] # up , down , left , right
	    direction[0] = 1
	    row,col = 0,0
	    result = []
	    while count<total:
	        result.append(A[row][col])
	        count+=1
	        if direction[0] :
	            if row==0:
	                direction[0]=0
	                direction[3]=1
                else :
	               row-=1
            	if direction[1] :
                    if row==m-1:
	                direction[1]=0
	                direction[2]=1
                else :
	               row+=1
	               
	        if direction[2] :
	            if col==0:
	                direction[2]=0
	                direction[0]=1
                else :
	               col-=1
	       
	        if direction[3] :
	            if col==n-1:
	                direction[3]=0
	                direction[1]=1
                else :
	               col+=1
        return result

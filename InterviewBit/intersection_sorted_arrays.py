'''
  Find the intersection of two sorted arrays.
  OR in other words,
  Given 2 sorted arrays, find all the elements which occur in both the arrays.
  Example :

  Input : 
      A : [1 2 3 3 4 5 6]
      B : [3 3 5]

  Output : [3 3 5]

  Input : 
      A : [1 2 3 3 4 5 6]
      B : [3 5]

  Output : [3 5]
'''
class Solution:
	# @param A : tuple of integers
	# @param B : tuple of integers
	# @return a list of integers
	
  # This could be a binary search function to reduce the time complexity from O(n) to O(logn)
  def find_ele(self,L,ele):
      for i in range(len(L)):
          if ele >= L[i]:
              return i
	
  # Since both the arrays are sorted , find out the intersection in range of both the arrays . 
  # Find the max of the first elements of both the arrays , the array with the max element will be part of the 
  # inner range of the other array , find out the starting point of that inner range using another function
  # run a while loop getting all the elements which are equal, increment the pointer of the array contaning min element
  # in each iteration.
	def intersect(self, A, B):
        l_A  = 0
        l_B = 0
        m = max(A[0],B[0])
        res= []
        if A[0]==m:
            l_B = self.find_ele(B,m)
        else :
            l_A = self.find_ele(A,m)
        
        while l_A < len(A) and l_B < len(B):
           if A[l_A] == B[l_B]:
               res.append(A[l_A])
               l_A += 1
               l_B += 1
           elif A[l_A] > B[l_B]:
               l_B += 1
           else :
               l_A += 1
        return res
	    

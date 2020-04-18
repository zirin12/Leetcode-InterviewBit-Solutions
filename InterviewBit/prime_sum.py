class Solution:
'''
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbach’s conjecture
'''

	# @param A : integer
	# @return a list of integers
  
  # create sieve and then find
  # can do it using normal way iterating to check for each num till square root limit
	def primesum(self, A):
	    prime = [1]*A
        prime[0] = 0
        prime[1] = 0
        prime[2] = 1
        num = 2
        while num*num <= A:
            if prime[num]==1:
                n = num
                n += num
                while n<A:
                    prime[n] = 0
                    n += num
            
            num += 1
        for j in range(2,A//2 + 1):
            if prime[j]==1:
                diff = A - j
                if prime[diff]==1:
                    return [j,diff]

'''
  For Given Number N find if its COLORFUL number or not

  Return 0/1

  COLORFUL number:

  A number can be broken into different contiguous sub-subsequence parts. 
  Suppose, a number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245. 
  And this number is a COLORFUL number, since product of every digit of a contiguous subsequence is different

  Example:

  N = 23
  2 3 23
  2 -> 2
  3 -> 3
  23 -> 6
  this number is a COLORFUL number since product of every digit of a sub-sequence are different. 

  Output : 1
'''

class Solution:
    # @param A : integer
    # @return an integer
    
    # Can try a different approach from the one below
    
    # Convert input to string,makes it easy to get subsequences in loop using slice
    # Make a hashmap for the products computed till now 
    # run two loops for all subsequences , calculate their product 
    # if it exists in hashmap return 0 else continue
    # after all the sub sequences are explored , return 1
    def colorful(self, A):
        prod_dict = {}
        S = str(A)
        n = len(S)
        for i in range(n):
            for j in range(i,n):
                num_str = S[i:j+1]
                prod = 1
                for char in num_str:
                    prod *= int(char)
                if prod in prod_dict:
                    return 0
                else :
                    prod_dict[prod] = 0
        return 1

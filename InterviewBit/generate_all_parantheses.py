'''
  Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem
'''

class Solution:
    # @param A : string
    # @return an integer
    
    # Use stack put opening symbols and for closing symbols pop and check
    def isValid(self, A):
        S = []
        B = {'}':'{',']':'[',')':'('}
        for sym in A:
            if len(S) == 0 and sym in B:
                return 0
            if sym in B.values():
                S.append(sym)
            else :
                if S.pop()!=B[sym]:
                    return 0
        if len(S) == 0:
            return 1
        else :
            return 0 

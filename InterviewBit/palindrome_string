'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example:

"A man, a plan, a canal: Panama" is a palindrome.

"race a car" is not a palindrome.

Return 0 / 1 ( 0 for false, 1 for true ) for this problem

'''

class Solution:
    # @param A : string
    # @return an integer
    
    # instead of continue everything can be done in if elif and else blocks
    def isPalindrome(self, A):
        n = len(A)
        l = 0
        h = n-1
        while l<=h and l<n and h>0:
            if not A[l].isalnum():
                l += 1
                continue
            
            if not A[h].isalnum():
                h -= 1
                continue
            
            if A[l].lower()!=A[h].lower():
                    return 0
            l += 1
            h -= 1
        return 1

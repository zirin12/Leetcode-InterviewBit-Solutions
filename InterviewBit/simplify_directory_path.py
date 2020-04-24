'''
Given a string A representing an absolute path for a file (Unix-style).

Return the string A after simplifying the absolute path.

Note:

    Absolute path always begin with ’/’ ( root directory ).

    Path will not have whitespace characters.


'''
class Solution:
    # @param A : string
    # @return a strings
    
    # Use stack and pop appropriately 
    # if proper stack is used the result of it's contents have to be reversed
    def simplifyPath(self, A):
        S = A.split('/')
        L  = []
        for sym in S:
            if sym == '..':
                if len(L)!=0:
                    L.pop()
            elif sym != '.' :
                L.append(sym)
        res = ""
        for sym in L:
            if sym!='':
                res = res + "/" + sym
            
        return res if res!="" else "/"

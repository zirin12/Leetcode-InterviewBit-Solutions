'''
  Given a digit string, return all possible letter combinations that the number could represent.

  A mapping of digit to letters (just like on the telephone buttons) is given below.

  The digit 0 maps to 0 itself.
  The digit 1 maps to 1 itself.

  Input: Digit string "23"
  Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

  Make sure the returned strings are lexicographically sorted.
'''

class Solution:
    # @param A : string
    # @return a list of strings
    
    # Make a dictionary of the mapping from digits to characters 
    # do the usual backtacking , where the base condition is the last element , return the mapping for that element
    # find all the combinations running two loop in order , one for the mapping of the current digit and the inner one 
    # for the last recursive call , this will give all combinations possible from the current index till the end in 
    # lexicographic order
    def all_combs(self,A,index,dig_alpha):
        if index == len(A)-1:
            return list(dig_alpha[A[index]])
        else :
            res = []
            last_combs = self.all_combs(A,index+1,dig_alpha)
            curr_dig = list(dig_alpha[A[index]])
            for char_c in curr_dig:
                for char_l in last_combs:
                    res.append("" + char_c + char_l)
            return res
    
    def letterCombinations(self, A):
        if len(A)==0 :
            return []
        dig_alpha = { 
            "0":"0",
            "1":"1","2":"abc","3":"def",
            "4":"ghi","5":"jkl","6":"mno",
            "7":"pqrs","8":"tuv","9":"wxyz"
        }
        res = self.all_combs(A,0,dig_alpha)
        return res

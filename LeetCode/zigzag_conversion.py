
'''
Given an input and number of rows , read line by line the zigzag pattern of the string.

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

'''

class Solution:
    # Find relation between diagonal elements and it's previous element in the zig zag representation
    # Code looks messy because of extra conditions to take care of special cases
    def convert(self, s: str, numRows: int) -> str:
        if(numRows > len(s)):
            return s
        output = ""
        gap = (numRows-2) if numRows>=2 else 0
        cols = ((len(s)//numRows) + gap) if gap>0 else ((len(s)//numRows) + 1) 
        diff = numRows + gap
        factor = 0
        for row in range(0,numRows):
            for col in range(0,cols):
                index = row + col*diff
                output = (output + s[index]) if index<len(s) else output
                if col <= (cols -1) and row > 0 and row < (numRows-1):
                    inner_index = index + diff - row - factor 
                    output  = (output + s[inner_index]) if inner_index < len(s) else output         
            factor+=1
        return output

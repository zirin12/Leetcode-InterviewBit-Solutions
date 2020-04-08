
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
    # This can be simplified by finding out the formula for getting each element in the row and then simplifying relations
    def convert_1(self, s: str, numRows: int) -> str:
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
    
    # simplest way ,decide the row each character belongs to by traversing characters in s with simple row variable tracker
    # and direction 
    def convert_2(self, s: str, numRows: int) -> str:
        if numRows == 1 :
            return s
        numRows = min(numRows,len(s))
        list_rows = [""]*numRows
        going_down = True
        curr_row = 0
        for char in s:
            list_rows[curr_row]+=char
            if going_down:
                curr_row+=1
            else:
                curr_row-=1
            
            if curr_row==0:
                going_down = True
            elif curr_row==numRows-1:
                going_down=False
            
        result = ""
        for string in list_rows:
            result+=string
        return result

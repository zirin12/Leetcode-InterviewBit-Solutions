"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:

    There may be more than one LIS combination, it is only necessary for you to return the length.
    Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
"""
class Solution:
    
    # INCOMPLETE 
    # implement recursion,recursion with memoization ,dp solution .
    
    # Used something called patience sort . 
    # In a new list . As we are looping over the input array , insert the number into the new list .
    # The number will be added at the position of the smallest largest number than itself (find_index does that here )
    # This ensures that we always cover the longest increasing subsequence by not missing out on any numbers after that or before that .
    # In the end the length of the new list will be the length of the longest increasing subsequence.
    # time complexity : O(n**2) , can be O(nlogn) if find_index is done using binary search . 
    def find_index(self, R, num) :
        index = len(R) - 1
        while index >= 0  and R[index] >= num:
            index -= 1
        return index + 1
    
    def lengthOfLIS(self, nums: List[int]) -> int:
        R = []
        for num in nums:
            if len(R) == 0 or num > R[-1]:
                R.append(num)
            else :
                index = self.find_index(R,num)
                R[index] = num
        return len(R)

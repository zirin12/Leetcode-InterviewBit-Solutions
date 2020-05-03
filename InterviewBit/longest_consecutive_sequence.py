'''
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Example:
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
class Solution:
    # @param A : tuple of integers
    # @return an integer
    
    # Can improve the below approach
    # add all numbers to a hash map
    # for each number look for the consecutive numbers greater and lesser than it using hash_map , also
    # delete the element in hash map if a number is found , to avoid repetetion of search
    # The time complexity of this solution will be KO(n) +/- M , where K and M are constants.So O(n) complexity
    def longestConsecutive(self, A):
        hash_map = {}
        for num in A :
            hash_map[num] = 0
        max_len = 1
        for num in A :
            if num in hash_map:
                curr_len = 1
                # for consecutive numbers greater than num
                num_g = num + 1
                while True:
                    if num_g in hash_map:
                        curr_len += 1
                        del hash_map[num_g]
                        num_g += 1
                    else :
                        break
                # for consecutive numbers lesser than num 
                num_l = num - 1
                while True:
                    if num_l in hash_map:
                        curr_len += 1
                        del hash_map[num_l]
                        num_l -= 1
                    else :
                        break
                max_len = max(curr_len,max_len)
                del hash_map[num]
        return max_len

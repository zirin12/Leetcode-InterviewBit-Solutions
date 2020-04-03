class Solution:
    # Two pass hash table
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        index = 0
        for num in nums :
            dict[num] = index
            index+=1
            
        index = 0 
        for num in nums:
            if (target - num) in dict.keys() and dict[target-num]!=index :
                return [index,dict[target-num]]
            index+=1
    
    # One pass hash table
    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        index = 0 
        for num in nums:
            if (target - num) in dict.keys() :
                return [index,dict[target-num]]
            else:
                dict[num] = index
            index+=1

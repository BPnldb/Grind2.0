class Solution(object):
    def twoSum(self, nums, target):
        """
        dic = {3:3, 2:2, }           }
        comp =  6 - 3 = 3
        comp = 6 - 2 = 4
        comp = 6 - 4 = 2
        """
        
        dic = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            
            if comp in dic:
                return [ dic[comp],i]
            else:
                dic[nums[i]] = i
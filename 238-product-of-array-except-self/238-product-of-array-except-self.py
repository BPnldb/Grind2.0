class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #returns an array
        
        res = len(nums) * [1]
        #[1,1,1,1]
        
        prefix , postfix = 1, 1
        
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        print(res)
        
        
        for i in range(len(nums) - 1, -1 , - 1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
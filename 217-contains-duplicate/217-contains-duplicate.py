class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dic = set()
        
        for i in range(len(nums)):
            if nums[i] in dic:
                return True
           
            dic.add(nums[i])
        return False
    
       
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq = set()
        
        for i in range(len(nums)):
            if nums[i] in freq:
                return True
            freq.add(nums[i])
        return False
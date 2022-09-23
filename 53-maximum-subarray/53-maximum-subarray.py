class Solution:
    def maxSubArray(self, nums):
        
        """
        Time: O(N)
        Space: O(1)
        """
        
        
        maxSum = nums[0] #[-2]
        windowSum = 0
        
        for i in range(len(nums)):
            if windowSum < 0:
                windowSum = 0
            windowSum+=nums[i]
            maxSum = max(maxSum, windowSum)
        return maxSum
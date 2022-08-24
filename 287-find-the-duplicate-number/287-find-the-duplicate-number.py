class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        Time Complexity : O(N)
        Space Complexity: O(1)
        
        """
        
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #reset slow to 0
        slow = 0
        
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]
        return fast
            
            
            
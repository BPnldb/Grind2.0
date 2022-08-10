class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #time: O(N)
        #space: O(N)
        # seen = {}
        # for i, nums in enumerate(numbers):
        #     difference = target - nums
        #     if difference not in seen:
        #         seen[nums] = i
        #     else:
        #         return [seen[difference]+1,i+1]
            
        
        left , right = 0 , len(numbers) - 1
        
        while left  < right:
            currentSum = numbers[left] + numbers[right]
            
            if currentSum > target:
                right -= 1
            elif currentSum < target:
                left += 1
            else:
                return [left + 1, right + 1]
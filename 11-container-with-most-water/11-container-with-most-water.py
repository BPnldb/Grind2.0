class Solution(object):
    def maxArea(self, height):
        """
        
        Time : O(N)
        space : O(1)
        :type height: List[int]
        :rtype: int
        """
        
        #brute force
#         result = 0
        
#         for l in range(len(height)):
#             for r in range(l + 1, len(height)):
#                 area = (r - l) * min(height[l], height[r])
#                 result = max(result, area)
#         return result


        result = 0
        left , right = 0 , len(height) - 1
        
        while left < right:
            area = (right - left) * min(height[left],height[right])
            result = max(result, area)
            
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return result
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
    
        left = 0
        right = len(height) - 1
        
        while left < right:
            area = abs(left-right) * min(height[left],height[right])
            result = max(area, result)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return result
class Solution(object):
    def threeSum(self, nums):
        
        
        
        #time complexity : O(N ^2) for nested loops (for and while)
        #space complexity : O(1), since it's iterating in place.
        
        #sort the array using some built in function
        #this is time complexity of O(nlogn)
        nums.sort()
        
        #initialize an empty list/array
        result = []
        
        #up to len(nums) - 2 because worse cause the solution would be 
        # [nums[i],nums[i-2],nums[i-1]]
        
        
        
        for left in range(len(nums) - 2):
            mid = left + 1
            right = len(nums) - 1
            
            while mid < right:
                curSum = nums[left] + nums[mid] + nums[right]
                sumList = [nums[left],nums[mid],nums[right]]
                
                if curSum == 0 and sumList not in result:
                    result.append(sumList)
                elif curSum < 0:
                    mid += 1
                else:
                    right -= 1
        return result
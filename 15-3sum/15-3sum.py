class Solution(object):
    def threeSum(self, nums):
        
        
        
        #time complexity : O(N ^2) for nested loops (for and while)
        #space complexity : O(1), since it's iterating in place.
        
        #sort the array using some built in function
        #this is time complexity of O(nlogn)
        nums.sort()
        
        #initialize an empty list/array
        tripleList = []
        
        #up to len(nums) - 2 because worse cause the solution would be 
        # [nums[i],nums[i-2],nums[i-1]]
        
        
        for i in range(len(nums)-2):
            left = i+1
            right = len(nums) -1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                sumList = [nums[i], nums[left] , nums[right]]
                
                #check if curSum is 0 and NOT IN tripleList
                if curSum == 0 and sumList not in tripleList:
                    tripleList.append(sumList)
                    left += 1
                    right -= 1
                elif curSum < 0:
                    left += 1
                else:
                    right -= 1
        return tripleList
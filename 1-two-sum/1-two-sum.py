class Solution:
    def twoSum(self, nums, target):
        hashMap = {}
        
        for i in range(len(nums)):
            compliment = target - nums[i] 
            #checks if c = 7 = 9 - 2
            #is in the hash, if not then continue
            if compliment in hashMap:
                return [hashMap[compliment],i]
            else:
                hashMap[nums[i]] = i #add the value to hash
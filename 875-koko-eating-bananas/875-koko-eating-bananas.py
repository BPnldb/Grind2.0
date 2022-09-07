class Solution(object):
    def minEatingSpeed(self, piles, h):
        
                
                
                
        """
        Optimized approach:
        
        
        
        
        Brute Force:
        
        Time: O(N*M) for speed x # of piles
        Space: O(1)
        """
        
        
        # speed = 1
        # while True:
        #     hour_spent = 0
        #     for pile in piles:
        #         hour_spent += math.ceil(pile*1.0 / speed)
        #         print(hour_spent)
        #     if hour_spent <= h:
        #         return speed
        #     else:
        #         speed += 1
        # print(speed)
        
        
        """
        Binary Search
        T:
        S:
        
        """
        
        left = 1
        right = max(piles)
        
        while left < right: #if they cross eachother
            mid = (left + right) // 2
            count = 0
            for i in piles:
                count += math.ceil(i * 1.0 / mid)
            if  count <= h:
                right = mid
            else:
                left = mid + 1
        return left
    
        
       
    
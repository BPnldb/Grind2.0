class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        Time:O(N)
        Space: O(1)
        Space:
        
        [10,15,20] 0
        
        """
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-2], cost[i-1])
            
        return min(cost[len(cost)-2], cost[len(cost)-1])
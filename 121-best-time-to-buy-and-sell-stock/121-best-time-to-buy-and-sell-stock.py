class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #Time Complexity: O(N)
        #Space COmplexity: O(1)
    
        #sliding window
        left , right = 0 ,1
        
        maxRes = 0
        
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            maxRes = max(maxRes, prices[right]-prices[left])
            right += 1
        return maxRes
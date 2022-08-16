class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        left, right = 0, 1
        maxRes = 0
        
        while right < len(prices):
            res = prices[right] - prices[left]
            if res < 0:
                left = right
            maxRes = max(maxRes, res)
            right += 1
        return maxRes
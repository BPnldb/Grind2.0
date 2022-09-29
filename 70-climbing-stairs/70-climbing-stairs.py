class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        Time Complexity : O(N)
        Space Complexity : O(1)
        """
        #Dynamic Programming
        if n == 0:
            return 0
        if n == 1:
            return 1
        a ,b = 1, 2
        
        
        """
        
        n = 5
        a=1
        b=2
        tmp = 2, b = 1 + 2 = 3, a = 2
        tmp = 3, b = 3 + 2 = 5, a = 3
        tmp = 5, b = 5 + 3 = 8, a = 5
        return b
        
        
        """
        
        
        
        for i in range (2, n): 
            tmp = b 
            b = a +b
            a = tmp
        return b
        

        #recursion
        """
        Time Complexity : O(2^N)
        Space COmplexity : O(N)
        """



        
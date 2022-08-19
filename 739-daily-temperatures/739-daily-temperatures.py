class Solution(object):
    def dailyTemperatures(self, temp):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        """
        O(N^2) Time, O(N) Space
        res = [0] * len(temperatures)
        for i in range(len(temperatures)-1):
            for j in range(i+1, len(temperatures)):
                if temperatures[i] < temperatures[j]:
                    res[i] = j-i
                    break
                    
        return res"""
        
        res = [0] * len(temp)
        stack = []
        
        
        for i in range(len(temp)):
            while stack and temp[i] > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                res[stackIndex] = (i - stackIndex)
            stack.append([temp[i],i])
        return res
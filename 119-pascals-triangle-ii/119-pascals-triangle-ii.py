class Solution(object):
    def getRow(self, r):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1] * (r+1)
        print(res)
        
        up = r
        down = 1
        
        for i in range(1, r):
            res[i] = res[i-1] * up/down
            up -= 1
            down +=1
        return res
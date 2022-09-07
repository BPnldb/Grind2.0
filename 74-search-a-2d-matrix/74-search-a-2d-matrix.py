class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        
        left and right pointer
        
        Time: O(LogN + logM)
        
        Space:O(1)
        """
        
        
        """
            R           R           R
        [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
           cccc     cccc            cccc 
           
          top = 1R
          bot = 3R
        """
        
        rows = len(matrix) # 3 rows
        cols = len(matrix[0]) # 4 columns 
        
        top = 0
        bot = len(matrix) - 1 
        
        while top <= bot:
            midRow = (top + bot) // 2
            if target > matrix[midRow][cols - 1]:
                top = midRow +1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                break
        if not (top <= bot):
            return False
        
        
        left = 0
        right = cols - 1
        
        while left <= right:
            mid = (left + right) //2
            if target > matrix[midRow][mid]:
                left = mid + 1
            elif target < matrix[midRow][mid]:
                right = mid - 1
            else:
                return True
        return False
        
      
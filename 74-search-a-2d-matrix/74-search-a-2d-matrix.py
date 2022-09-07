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
        
        #two Binary Search (inner)
        rows, cols = len(matrix), len(matrix[0])
        
        #binary search outer of rows 
        top = 0
        bot = rows - 1
        
        
        while top <= bot:
            midRow = top + ((bot - top) // 2)
            print(matrix[midRow][cols-1])
            if target > matrix[midRow][cols - 1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                break
                
        if not (top <= bot):
            return False
        
        
        left = 0
        right = cols - 1
        
        while left <= right:
            mid = left + ((right - left) //2)
            if target > matrix[midRow][mid]:
                left = mid + 1
            elif target < matrix[midRow][mid]:
                right = mid - 1
            else:
                return True
        return False
        
      
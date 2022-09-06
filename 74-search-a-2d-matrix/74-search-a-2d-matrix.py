class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        
        left and right pointer
        
        Time: O(LogN + logM)
        
        Space:O(1)
        """
        
        #two Binary Search (inner)
        rows, cols = len(matrix), len(matrix[0])
        
        #binary search outer of rows 
        top = 0
        bot = rows - 1
        
        
        while top <= bot:
            midRow = (top + bot) // 2
            if target > matrix[midRow][cols - 1]:
                top = midRow + 1
            elif target < matrix[midRow][0]:
                bot = midRow - 1
            else:
                break
                
        if not (top <= bot):
            return False
        
        
        midRow = (top + bot) // 2
        left, right = 0, cols -1 #right = right most position in the row
        
        while left <= right:
            mid = (left + right) // 2
            if target > matrix[midRow][mid]:
                left = mid + 1
            elif target < matrix[midRow][mid]:
                right = mid - 1
            else:
                return True
            
        return False
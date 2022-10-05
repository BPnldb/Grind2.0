class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        """
        Brute force O(N^2), s = O(1)
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == target:
                    return True
        return False"""
        
        
        r = 0
        c = len(matrix[0]) - 1
        while r < len(matrix) and c >= 0:
            if target == matrix[r][c]:
                return True
            elif matrix[r][c] < target:
                r += 1
            else:
                c -= 1
        return False
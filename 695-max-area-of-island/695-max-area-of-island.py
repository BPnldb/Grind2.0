class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # have a visit hash set to mark positions we already visited
        #T: O(M * N)
        
        ROWS , COLS =  len(grid), len(grid[0])
        visit = set()
        
        def dfs(r, c): #position we pass in
            #base case out of bounds
            if (r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == 0 or (r,c) in visit):
                return 0
            
            visit.add((r,c))
            return (1 + dfs(r + 1,c)+
                        dfs(r - 1, c)+
                        dfs(r, c + 1)+
                        dfs(r, c - 1))
        
        area = 0
        
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r,c))
        return area
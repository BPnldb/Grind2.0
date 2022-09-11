class Solution:
    def combinationSum(self,candidates, target):
        res = []
        res2 = []
        #[2,2,3],[2,2,2]
        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            #candidates[i]
            cur.append(candidates[i])
            dfs(i, cur, total + candidates[i])
            cur.pop()
            dfs(i + 1, cur, total)
            
        dfs(0, res2, 0)
        return res
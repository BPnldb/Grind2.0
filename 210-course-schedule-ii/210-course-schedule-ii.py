class Solution:
    def findOrder(self, numCourses, pre):
        #DFS
        
        adj_list = {i:[] for i in range(numCourses)}
        
        for u, v in pre:
            adj_list[u].append(v)
        
        res = []
        
        visit = set()
        cycle = set()
        
        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            
            cycle.add(node)
            for i in adj_list[node]:
                if dfs(i) == False:
                    return False
        
            cycle.remove(node)
            visit.add(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res
class Solution:
    def canFinish(self, numCourses, pre):
        adj_list = {i:[] for i in range(numCourses)}
        
        for u,v in pre:
            adj_list[u].append(v)
        
        visited = set()
        
        def dfs(course):
            if course in visited:
                return False
            
            if adj_list[course] == []:
                return True
            
            visited.add(course)
            
            for p in adj_list[course]:
                result = dfs(p)
                if not result:
                    return False
            visited.remove(course)
            adj_list[course] = []
            return True
            
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
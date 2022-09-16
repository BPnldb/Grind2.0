class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adj_list = {i:[] for i in range(numCourses)}
        
        for u, v in prerequisites:
            adj_list[u].append(v)
        print(adj_list)
        
        visited = set() #shows visited vertex already
        cycle = set() #detects a cycle
        res = []
        #so once we have created our adjacency list, we can get started with the DFS
        
        
        
        
        def dfs(node):
            #check if in cycle
            #check if in visited
            #if no conditions then continue
            #add node to cycle
            
            #loop through the node's neighbors and call DFS
                #check if it returns true or false
                #if false then break immediately 
            #if all else is TRUE, then
            #remove from cycle
            #add to visited
            #append to result
            #return true
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            
            for neigh in adj_list[node]:
                if dfs(neigh) == False:
                    return False
                
            cycle.remove(node)
            visited.add(node)
            res.append(node)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res
            
            
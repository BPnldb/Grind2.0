from collections import deque,defaultdict
class Solution:
    def findOrder(self, numCourses, prerequisites):
        #DFS
        
        #-----
        
        
        #BFS
        
        #indegree #arrows pointing to it
        adj_list = defaultdict(list)
        indegree = [0] * numCourses
        
        for pre, final in prerequisites:
            adj_list[pre].append(final)
            indegree[final] += 1
        print(adj_list)
        print(indegree)
        #only if the node with an indegre of 0.
        #so if the node has nothing pointing to it
        q = deque([i for i in range(numCourses) if indegree[i] == 0])
        print(q)
        
        topologicalSortedOrder = []
        
        while len(q):
            node = q.popleft()
            topologicalSortedOrder.append(node)
            
            #decrease the neighbor's node by 1 
            for nei in adj_list[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        return topologicalSortedOrder[::-1] if len(topologicalSortedOrder) == numCourses else []
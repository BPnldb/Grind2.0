class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        #DFS
#         adj_list = {i:[] for i in range(numCourses)}
#         for u,v in pre:
#             adj_list[u].append(v)
        
#         visited = set()
        
#         def dfs(course):
#             if course not in visited:
#                 if adj_list[course] == []:
#                     return True

#                 visited.add(course)

#                 for p in adj_list[course]:
#                     result = dfs(p)
#                     if not result:
#                         return False
#                 visited.remove(course)
#                 adj_list[course] = []
#                 return True

#                 for course in range(numCourses):
#                     if not dfs(course):
#                         return False
#                 return True
#             return False
        #BFS
    
        visited = [0] * numCourses
        graph = defaultdict(list)
        for courses in prerequisites:
            graph[courses[1]].append(courses[0])
            visited[courses[0]] += 1
            
        # find a node with no incoming edge and add it to queue.
        queue = deque()
        for i in range(numCourses):
            if visited[i] == 0:
                queue.append(i)
                
        # topological sort algorithm - bfs approach.
        total_courses = 0
        while queue:
            course = queue.popleft()
            total_courses += 1
            for prerequisite in graph[course]:
                visited[prerequisite] -= 1
                if visited[prerequisite] == 0:
                    queue.append(prerequisite)
                    
        return total_courses == numCourses
            
        
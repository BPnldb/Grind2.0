from collections import deque, defaultdict

class Solution():
    def validPath(self, n,edges, source, destination):
        """
        
        BFS
        Time: O(N)
        Space: O(N)
        
        
        """
#         #1 create adjacency list
#         adj_list = defaultdict(list) #dictionary of list
#         q = deque([source])
#         visited = set() #visited so we don't revisit them. Starts with 0 because source

       
        
#         for u, v in edges:
            
#             adj_list[u].append(v)
#             adj_list[v].append(u)
#         print(adj_list)
        
        
#         while q:
#             node = q.popleft()
#             if node == destination:
#                 return True
            
#             for neighbor in adj_list[node]:
#                 # print(adj_list[node]) # prints list of values
#                 # print(neighbor) #prints values in the list
                
#                 if neighbor not in visited:
#                     #append that vertex to visited and then add that to the queue to search it's adjacent nodes.
#                     visited.add(neighbor)
#                     q.append(neighbor)
                    
#         return False
        
        
        
        
        """
        DFS
        """
        adj_list = defaultdict(list)
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        visited = set() #put the source in visited set
        
        
        
        
        def dfs(node):
            if node == destination:
            
                return True
            if node not in visited:
                visited.add(node)
                
                for neighbor in adj_list[node]:
                    result = dfs(neighbor)

                    if result:
                        return True
                    
        return dfs(source)
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parent = [-1] * (len(edges) + 1)
        
        def find(node):
            while parent[node] > 0:
                node = parent[node]
            return node
        
        def union(node1, node2):
            one, two = find(node1), find(node2)
            
            if one == two:
                return False
            
            else:
                parent[one] = two
                return True
            
        for u, v in edges:
            if not union(u,v):
                return [u,v]
g = Solution()
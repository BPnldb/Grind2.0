class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)
        
        def find(node):
            p = par[node]
            while p != par[p]:
                #par[p] = par[par[p]]
                p = par[p]
            return p
        
        #return false if can't complete (already merged)
        def union(node1, node2):
            p1, p2 = find(node1), find(node2)
            
            if p1==p2:
                return False
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
        
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
    
        for node1, node2 in edges:
            if not union(node1, node2):
                return [node1, node2]
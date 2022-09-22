# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, node, val):
        #dfs
        #root exist
        #root = val
        #dfs 
        
        
        def dfs(root):
            if root is None:
                return
            if root.val == val:
                return root
            return dfs(root.left) or dfs(root.right)
    
        
        return dfs(node)
       
        
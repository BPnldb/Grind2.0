# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root, val):
        #dfs
        #root exist
        #root = val
        #dfs 
        
        
        if root is None:
            return
        if root.val == val:
            return root
        
        return self.searchBST(root.left,val) or self.searchBST(root.right,val)
       
        
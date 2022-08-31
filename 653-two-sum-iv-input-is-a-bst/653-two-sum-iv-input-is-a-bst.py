# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        """
        target = k
        return true if two elements in bst = K
        
        """
        
        self.vals = {}
        
        
        def dfs(node):
            if not node:
                return False
            
            if node.val in self.vals:
                return True
            
            self.vals[k - node.val] = True
            
                
            return dfs(node.left) or dfs(node.right)
        return dfs(root)
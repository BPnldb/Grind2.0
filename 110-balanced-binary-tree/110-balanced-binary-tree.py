# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def dfs(root):
            if not root:
                
                return (True,0)
            i,left = dfs(root.left)
            j,right = dfs(root.right)
            
            
            #balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1
            
            return (i and j and abs(left-right) <=1, 1 +max(left,right))
        return dfs(root)[0]
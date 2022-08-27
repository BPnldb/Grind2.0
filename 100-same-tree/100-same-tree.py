#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        
        Time: O(N)
        Space : O(N)
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
        
        def dfs(i,j):
            if not i and not j:
                return True
            if not i or not j:
                return False
            if i.val != j.val:
                return False
            return dfs(i.left,j.left) and dfs(i.right, j.right)
        return dfs(p,q)
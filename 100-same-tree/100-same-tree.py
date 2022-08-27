#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        def dfs(i,j):
            if not i and not j:
                return True
            elif not i or not j:
                return False
            elif i.val == j.val:
                return dfs(i.left, j.left) and dfs(i.right, j.right)
            else:
                return False
        return dfs(p,q)
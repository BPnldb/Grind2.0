# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        
        
        

        def isSameTree(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val != q.val:
                return False
            return isSameTree(p.left,q.left) and isSameTree(p.right,q.right)
        

        def dfs(root, subroot):
            if not root:
                return False
            if not subroot:
                return True
            if isSameTree(root,subroot):
                return True
            left = dfs(root.left, subroot)
            right = dfs(root.right,subroot)
            return left or right
        return dfs(root,subRoot)
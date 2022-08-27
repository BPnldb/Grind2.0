# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        
        if not subRoot:
            return True
        if not root:
            return False
        
        
        def isSameTree( p, q):

            #recursion

            #if both are None
            if not p and not q:
                return True

            #if one or the other is None
            if not p or not q:
                return False

            #if the values do not match
            if p.val != q.val:

                return False
            return (isSameTree(p.left,q.left) and isSameTree(p.right,q.right))
        
        if isSameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
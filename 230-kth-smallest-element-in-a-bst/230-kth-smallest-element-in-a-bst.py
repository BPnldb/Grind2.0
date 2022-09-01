# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        res = []
        def _inorder(node):
            if not node: return
            _inorder(node.left)
            if len(res) == k:
                return
            res.append(node.val)
            _inorder(node.right)
        _inorder(root)
        return res[-1]
            
                
                
        
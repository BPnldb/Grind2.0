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
        def inorder(node,vals):
            if not node:
                return
            
            inorder(node.left,vals)
            vals.append(node.val)
            inorder(node.right, vals)
        inorder(root, res)
        print(res)
        return res[k-1]
            
                
                
        
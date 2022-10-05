# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        
        def dfs(node, pee, qq):
            while node:
                if pee.val > node.val and qq.val > node.val:
                    node = node.right
                elif pee.val < node.val and qq.val < node.val:
                    node = node.left
                else:
                    return node
        return dfs(root, p, q)
            
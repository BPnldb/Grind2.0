# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        #iteratively
        
        stack = [root]
        while stack:
            node = stack.pop()
            clay = node
            if clay:
                clay.left, clay.right = clay.right, clay.left

                stack.append(node.right)
                stack.append(node.left)
        return root
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
#         def dfs(node, maxVal):
#             if not node:
#                 return 0
            
#             if node.val >= maxVal :
#                 res = 1
#             else:
#                 res = 0
#             maxVal = max(node.val, maxVal)
            
#             res += dfs(node.left, maxVal)
#             res += dfs(node.right, maxVal)
            
#             return res
#         return dfs(root, root.val)

        self.count = 0
        def dfs(node, maxVal):
    
        
            if not node:
                return 0
            if node.val >= maxVal:
                self.count += 1
            maxVal = max(maxVal, node.val)

            dfs(node.left, maxVal)
            dfs(node.right, maxVal)

        
        dfs(root, root.val)
        return self.count
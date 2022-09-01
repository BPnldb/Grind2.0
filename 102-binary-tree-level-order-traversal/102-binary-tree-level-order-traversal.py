# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        
        res = []
        if not root:
            return []
        q = deque([root])
        while q:
            values = []
            for i in range(len(q)):
                
                node = q.popleft()
                
                # if node.left:
                #     q.append(node.left)
                # if node.right:
                #     q.append(node.right)
                

                if node:
                    values.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if values:
                res.append(values)
        return res
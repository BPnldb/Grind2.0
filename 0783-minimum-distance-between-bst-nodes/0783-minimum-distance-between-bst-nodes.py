# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node,result):
            if not node:
                return
            dfs(node.left,result)
            result.append(node.val)
            dfs(node.right,result)
            
            return
        
        
        res = []
        minimum = float('inf') 
        dfs(root,res)
        for i in range(1,len(res)):
            minimum = min(minimum,res[i]-res[i-1])
        return minimum
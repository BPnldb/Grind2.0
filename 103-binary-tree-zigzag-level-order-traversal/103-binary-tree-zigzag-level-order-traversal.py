from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        check if root. if empty then return empty list
        check if root has any children else print itself
        3, [20,9],[15,7]
        -keep a flag to change true/false when we iterate through the levels
            - if True, then swap
            -if False, then don't swap
        level order using a queue
        -next level
            -check if each node has children 
        
        
        """
        flag = False
        res = []
        
        q = deque()
        if root:
            q.append(root)
        while q:
            swapList = []
            for i in range(len(q)):
                node  = q.popleft()
                if node:
                    
                    
                    swapList.append(node.val)
                    
                    if node.left:
                        q.append((node.left))
                    if node.right:
                        q.append((node.right))
            if flag:
                flag = False
                res.append(reversed(swapList))
            else:
                flag = True
                res.append(swapList)

            
                    
                    
            
        return res

            
                
                
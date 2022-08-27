#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        
        """
        T:O(N)
        S:O(H)
        def dfs(i,j):
            if not i and not j:
                return True
            elif not i or not j:
                return False
            elif i.val == j.val:
                return dfs(i.left, j.left) and dfs(i.right, j.right)
            else:
                return False
        return dfs(p,q)
        
        """
        stack = [[p,q]]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif None in [node1,node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append([node1.left,node2.left])
                stack.append([node1.right,node2.right])
        return True
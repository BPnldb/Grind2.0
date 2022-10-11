# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        Time: O(N)
        Space: O(LogN) because balanced
        -Array is sorted
        -middle can be the root
        -use recursion to work sub problems
        """
        
        def dfs(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            
            root = TreeNode(nums[mid]) #middle of array is the root node
            
            root.left = dfs(left, mid - 1) #start at begininng of array and left of mid
            root.right = dfs(mid+1, right) #start at mid+1 to end of array
            
            return root
        
        return dfs(0, len(nums)-1)
    
    """
    
         0
        / \
      -10
      /
     
    
    
    """
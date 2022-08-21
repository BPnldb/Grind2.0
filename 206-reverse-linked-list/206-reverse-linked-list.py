# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
       
    
        """
        -break down into sub probs
        -instead of entire LL, reverse the remainder
         
        """

        
        #Time Complexity : O(N)
        #Space Complexity : O(N)
    
        start = None
        while head:
            temp = head.next
            head.next  = start
            start  = head
            head = temp
        return start
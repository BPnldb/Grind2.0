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
         
        

        
        #Time Complexity : O(N)
        #Space Complexity : O(1)
    
        start = None
        while head:
            temp = head.next
            head.next  = start
            start  = head
            head = temp
        return start
        
        """
        
        #recursive
        # T:O(N)
        # S:O(N) creates new memory stack every time it calls itself.
        
        #base case
        if not head or not head.next:
            return head
        current = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return current
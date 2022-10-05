# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptr1, ptr2 = headA, headB
        
        while ptr1 != ptr2:
            ptr1 = headB if ptr1 is None else ptr1.next
            ptr2 = headA if ptr2 is None else ptr2.next
        
        return ptr1
       
            
      
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        
        #Time Complexity: O(N)
        #Space Complexity : O(1)
        
        #find middle
        slow, fast = head, head
        
        while fast and fast.next:
            #shift pointers
            slow = slow.next
            fast = fast.next.next 
             
                
        #reverse second half
        mid = slow.next #holds the 2nd half of list
        slow.next = None #set to None now.
        prev = None
        
        
        while mid:
            next = mid.next
            mid.next  = prev
            prev = mid
            mid = next
        #merge two halfs together
        first = head
        second = prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
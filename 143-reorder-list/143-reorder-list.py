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
        slow,fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
             
                
        #reverse second half
        mid = slow.next
        slow.next = None
        prev = None
        
        while mid:
            nextNode = mid.next
            mid.next = prev
            prev = mid
            mid = nextNode
            
        
        
        
        #merge two halfs together
        first = head
        second = prev
        while second:
            temp1 , temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first,second = temp1, temp2
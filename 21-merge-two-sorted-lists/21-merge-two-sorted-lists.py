# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        current = head
        
        print(current)
        while l1 and l2:          #check if both lists are empty
            if l1.val <= l2.val:    #if value in each list is <= eachother.
                current.next = l1   # if yes then set current.next to that value.
                l1 = l1.next        #update l1's value to the next value.
            else:
                current.next = l2  #do same if l2 is smaller than l1's value.
                l2 = l2.next
            current = current.next   #update current's value to the next value to be stored.
            
        if l1:
            current.next = l1
        else:
            current.next = l2
        return head.next
        
            
            
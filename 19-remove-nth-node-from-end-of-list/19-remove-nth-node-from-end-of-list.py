# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        li = []
		
        while head:
            li.append(head)
            head = head.next
        
        if len(li) == 1:
            return None
        
        i = len(li)-n
        if i == 0:
            return li[1]
        elif i == len(li)-1:
            li[i-1].next = None
        else:
            li[i-1].next = li[i+1]
        
        return li[0]
        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        len = 0
        p = head
        while p is not None:
            p = p.next
            len += 1
            
        if len == n:
            return head.next
        
        p = head
        i = 0
        while i < len-n-1:
            p = p.next
            i += 1
                
        p.next = p.next.next        

        return head
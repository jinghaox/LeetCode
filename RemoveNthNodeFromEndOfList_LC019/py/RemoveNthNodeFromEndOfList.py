# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        first get the len of the list, needs to traverse the list once
        then loop to len-n-1 node, remove the nth node
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
    
    def removeNthFromEndSmart(self, head, n):
        """
        first move to nth node from the head
        then move pre(None), cur(Head), and nth node all together
        when nth node reaches the end, remove the cur node, that's it
        """
        if head is None:
            return []
        
        pre, cur, nth = None, head, head
        for i in range(n):
            if nth is not None:
                nth = nth.next
        
        while nth is not None:
            pre = cur
            cur = cur.next
            nth = nth.next
        
        if pre is None and cur.next is None:
            return []
        elif pre is None:
            return head.next
        else:
            pre.next = cur.next

        return head


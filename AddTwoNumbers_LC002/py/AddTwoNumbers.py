# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        newVal = l1.val + l2.val
        if newVal >= 10:
            newVal = newVal%10
            carry = 1
        head = ListNode(newVal)

        cur = head 
        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            newVal = l1.val + l2.val + carry
            if newVal >= 10:
                newVal -= 10
                carry = 1
            else:
                carry = 0
            cur.next = ListNode(newVal) 
            cur = cur.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            cur.next = ListNode(l1.val + carry)
            cur = cur.next
            l1 = l1.next
            carry //= 10

        while l2:
            cur.next = ListNode(l2.val + carry)
            cur = cur.next
            l2 = l2.next
            carry //= 10
        
        if carry == 1: 
            cur.next = ListNode(1)

        return head

    def createLinkedListFromNum(self, num):

        # create head of a linked list using the last digit
        n = num % 10
        head = ListNode(n)

        # set up current node
        cur = head

        # update the number by removing the last digit, e.g. 342 --> 34
        num = num//10

        # loop the remaining number, append the last digit to the linked list
        while num:
            n = num % 10
            node2 = ListNode(n)
            cur.next = node2
            cur = cur.next
            num = num//10

        return head

    def printLinkedList(self, linkedList):
        print("\nHere is the linked list content")
        while linkedList:
            print("{}->".format(linkedList.val), end='')
            linkedList = linkedList.next


s = Solution()
linkedList1 = s.createLinkedListFromNum(545)
s.printLinkedList(linkedList1)
linkedList2 = s.createLinkedListFromNum(565)
s.printLinkedList(linkedList2)
newLinkedList = s.addTwoNumbers(linkedList1, linkedList2)
s.printLinkedList(newLinkedList)

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    
    def __repr__(self):
        if not self:
            return 'Null'
        else:
            # here call repr(ListNode)
            return "{}->{}".format(self.val, repr(self.next))

class LinkedList(object):
    """
    Create a new class of LinkedList is ok
    But it doesn't meet the LeetCode's requirements: where the rtype of addTwoNumbers() needs to be a ListNode, not LinkedList
    And Leet Code can't know we have a new class LinkedList defined
    """
    def __init__(self):
        # create a class's variable, so it will be shared by all member functions
        # we don't need to return it in each member function
        self.head = None
    
    def insertNodeToHead(self, val):
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
    
    def insertNodeToTail(self, val):
        p = self.head
        newNode = ListNode(val)
        if p is None:
            self.head = newNode
        else:
            while p.next:
                p = p.next
        
            p.next = newNode 
    
    def printLinkedList(self):
        print("\nPrint out linked list: ")
        p = self.head
        while p:
            print("{}->".format(p.val), end='')
            p = p.next 
        print("nil")

    def createLinkedListFromNum(self, num):
        while num:
            n = num % 10
            self.insertNodeToTail(n)
            num = num//10
        return self.head


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
            newVal %= 10
            carry = 1
        head = ListNode(newVal)

        l1 = l1.next
        l2 = l2.next

        cur = head
        while l1 or l2:
            newVal = 0 
            if l1:
                newVal += l1.val
                l1 = l1.next
            if l2:
                newVal += l2.val
                l2 = l2.next
            newVal += carry

            if newVal >= 10:
                newVal %= 10
                carry = 1
            else:
                carry = 0

            cur.next = ListNode(newVal)
            cur = cur.next
       
        if carry == 1: 
            cur.next = ListNode(1)

        return head 

    def addTwoNumbersUsingLinkedListClass(self, l1, l2):
        newList = LinkedList()
        carry = 0
        newVal = l1.val + l2.val
        if newVal >= 10:
            newVal -= 10
            carry = 1
        newList.insertNodeToTail(newVal)

        l1 = l1.next
        l2 = l2.next

        while l1 and l2:
            newVal = l1.val + l2.val + carry
            if newVal >= 10:
                newVal -= 10
                carry = 1
            else:
                carry = 0
            newList.insertNodeToTail(newVal)
            l1 = l1.next
            l2 = l2.next

        while l1:
            newList.insertNodeToTail(l1.val + carry)
            l1 = l1.next
            carry //= 10

        while l2:
            newList.insertNodeToTail(l2.val + carry)
            l2 = l2.next
            carry //= 10
        
        if carry == 1: 
            newList.insertNodeToTail(1)

        return newList.head 


s = Solution()
lList1 = LinkedList()
l1 = lList1.createLinkedListFromNum(789)
lList2 = LinkedList()
l2 = lList2.createLinkedListFromNum(456)
print(l1)
print(l2)
x = s.addTwoNumbers(l1, l2)
print(x)
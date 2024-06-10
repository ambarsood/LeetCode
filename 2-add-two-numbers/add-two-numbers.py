# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            if l1 is not None:
                digit1 = l1.val
            else:
                digit1 = 0

            if l2 is not None:
                digit2 = l2.val
            else:
                digit2 = 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            if l1 is not None:
                l1 = l1.next
            else:
                l1 = None

            if l2 is not None:
                l2 = l2.next
            else:
                l2 = None

        result = dummyHead.next
        dummyHead.next = None
        return result
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1,n2="",""
        while l1:
            n1=str(l1.val) + n1
            l1=l1.next
        while l2:
            n2=str(l2.val) + n2
            l2=l2.next
        if not n1:
            n1="0"
        if not n2:
            n2="0"

        summ= int(n1)+int(n2)

        dummyHead = ListNode(0)
        tail = dummyHead

        for i in reversed(str(summ)):
            tail.next=ListNode(int(i))
            tail=tail.next
        return dummyHead.next            




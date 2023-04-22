# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = ListNode(0)
        temp.next = head
        l = m = temp
        for i in range(n):
            m = m.next
        while m.next:
            l = l.next
            m = m.next
        l.next = l.next.next
        return temp.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            previous = None
            current = head
            while current:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node
            return previous

        l1 = reverse(l1)
        l2 = reverse(l2)
        dummy = ListNode()
        current = dummy
        temp = 0
        while l1 or l2 or temp:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + temp
            temp = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        result = reverse(dummy.next)
        return result
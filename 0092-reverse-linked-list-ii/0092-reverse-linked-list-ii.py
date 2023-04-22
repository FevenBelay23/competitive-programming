# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return None
        previous = None
        current = head
        for i in range(1, left):
            previous = current
            current = current.next
        first = previous
        second = current
        
        for i in range(left, right+1):
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        if first:
            first.next = previous
        else:
            head = previous
        second.next = current
        return head
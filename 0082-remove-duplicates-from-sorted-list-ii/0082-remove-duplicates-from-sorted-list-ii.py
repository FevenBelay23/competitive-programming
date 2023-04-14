# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        remove = ListNode(-1)
        remove.next = head
        previous, current = remove, head
        while current:
            if current.next and current.next.val == current.val:
                while current.next and current.next.val == current.val:
                    current = current.next
                current = current.next
            else:
                previous.next = current
                previous = previous.next
                current = current.next
        previous.next = None
        return remove.next
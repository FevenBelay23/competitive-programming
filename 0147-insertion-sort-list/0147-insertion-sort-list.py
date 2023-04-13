# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        Sort = None
        while head:
            node = head
            head = head.next
            if not Sort or node.val < Sort.val:
                node.next = Sort
                Sort = node
            else:
                current = Sort
                while current.next and current.next.val < node.val:
                    current = current.next
                node.next = current.next
                current.next = node
        return Sort
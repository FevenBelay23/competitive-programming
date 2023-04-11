# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        i = j = head
        while j and j.next:
            i = i.next
            j = j.next.next
        previous = None
        current = i
        while current:
            current.next, previous, current = previous, current, current.next
        while previous and head:
            if previous.val != head.val:
                return False
            previous, head = previous.next, head.next
        return True
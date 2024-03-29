# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        j = head
        while j and j.next:
            i = i.next
            j = j.next.next
            if i == j:
                temp = head
                while temp != i:
                    temp = temp.next
                    i = i.next
                return temp
        return None
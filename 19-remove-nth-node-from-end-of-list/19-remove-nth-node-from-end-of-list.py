# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        first = ListNode(0, head)
        left = first
        right = head
        while n>0 and right:
            right = right.next
            n-= 1
        while right:
            left = left.next
            right = right.next 
        left.next = left.next.next
        return first.next  
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        temp = head
        cnt = 0
        while temp:
            temp = temp.next
            cnt += 1
        prev = tail = ListNode(0, head)
        for i in range(cnt// k):
            start = prev
            for j in range(k):
                head.next, head, prev = prev, head.next, head
            start.next.next = head
            start.next, prev = prev, start.next
        return tail.next
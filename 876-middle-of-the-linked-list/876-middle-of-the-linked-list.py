# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        List = []
        while current is not None:
            List.append(current.val)
            current = current.next
        if len(List) % 2 == 0:
            mid = (len(List) + 1)//2
        else:
            mid = len(List) // 2
        i = 0
        while i != mid:
            i += 1
            head = head.next    
        return head
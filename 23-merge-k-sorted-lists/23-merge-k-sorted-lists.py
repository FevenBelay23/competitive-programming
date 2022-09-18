# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        self.nodes = []
        head = result = ListNode(0)
        for i in lists:
            while i:
                self.nodes.append(i.val)
                i = i.next
        for j in sorted(self.nodes):
            result.next = ListNode(j)
            result = result.next
        return head.next
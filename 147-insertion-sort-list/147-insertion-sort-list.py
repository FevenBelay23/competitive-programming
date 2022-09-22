# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tail = ListNode(0, head)
        previousI = tail
        i=head
        while i:
            previousJ, j = tail, tail.next
            while j.val < i.val:
                previousJ, j = j, j.next

            if i is j:
                previousI, i = i, i.next
            else:
                previousI.next = i.next
                i.next = j
                previousJ.next = i
                i = previousI.next
  
        return tail.next
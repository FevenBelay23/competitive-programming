# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head=ListNode()
        first=head
        Sum=0
        while(l1 or l2 or Sum!=0):
            if l1:
                Sum=Sum+l1.val
                l1=l1.next
            if l2:
                Sum=Sum+l2.val
                l2=l2.next
            sec=ListNode()
            sec.val=Sum%10 
            first.next=sec
            first=sec 
            Sum=int(Sum/10)
        return head.next
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lst=[]
        def palin(head):
            lst.append(head.val)
            if head.next:
                head=head.next
                palin(head)
            return
        palin(head)
        if lst==lst[::-1]:
            return True
        return False
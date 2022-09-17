# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous = None
        current = head
        while(current != None):
            check = False
            while(current.next != None and current.val == current.next.val):
                current, check = current.next, True
            if(check):
                if(previous == None):
                    head = current.next
                else:
                    previous.next = current.next
            else:
                previous = current
            current = current.next
        return(head)
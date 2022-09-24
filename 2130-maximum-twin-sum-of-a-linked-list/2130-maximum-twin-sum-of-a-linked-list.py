# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        start= head
        i=0
        while start:
            i+=1
            start=start.next
        start=head
        j= i//2
        while start and j:
            start = start.next
            j-=1
        previous = None
        while start:
            temp=start.next
            start.next=previous
            previous=start
            start=temp
        answer = previous.val+head.val
        while previous:
            k=previous.val+head.val
            answer=max(answer,k)
            previous=previous.next
            head = head.next   
        return answer
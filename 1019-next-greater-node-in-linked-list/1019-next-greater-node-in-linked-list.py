# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        cnt= 0
        i= head
        while i:
            cnt+= 1
            i = i.next
        answer=[0]*cnt
        stack =[]
        j=head
        k = 0
        while j:
            current= j.val
            while stack and stack[len(stack) - 1][1] <current:
                idx = stack[-1][0]
                answer[idx] = current
                stack.pop()
            stack.append([k, j.val])
            j= j.next
            k = k+1
        return answer
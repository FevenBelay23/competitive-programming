# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = []
        for i, j in enumerate(lists):
            if j:
                heapq.heappush(temp, (j.val, i))
                lists[i] = j.next
        ascend = ListNode(0)
        current = ascend
        while temp:
            val, i = heapq.heappop(temp)
            current.next = ListNode(val)
            current = current.next
            if lists[i]:
                heapq.heappush(temp, (lists[i].val, i))
                lists[i] = lists[i].next
        return ascend.next
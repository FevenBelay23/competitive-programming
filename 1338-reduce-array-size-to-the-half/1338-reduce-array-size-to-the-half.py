class Solution(object):
    def minSetSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        List={}
        for i in arr:
            if i in List:
                List[i] += 1
            else:
                List[i] = 1         
        stack = []
        for j in List:
            stack.append(List[j])   
        stack.sort()
        temp = stack[::-1]
        removed = 0
        size = 0
        mid = (len(arr)) // 2
        for k in temp:
            removed += k
            size += 1
            if removed >= mid:
                break
        return size
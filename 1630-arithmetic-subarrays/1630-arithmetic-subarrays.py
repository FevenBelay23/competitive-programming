class Solution(object):
    def checkArithmeticSubarrays(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: List[int]
        :type r: List[int]
        :rtype: List[bool]
        """
        answer = []
        for i in range(len(l)):
            temp = nums[l[i]:r[i]+1]
            temp.sort()
            diff = temp[1] - temp[0]
            check = False
            for j in range(1, len(temp)):
                if temp[j]-temp[j-1] != diff:
                    check = True
                    break
            if check:
                answer.append(False)
            else:
                answer.append(True)
        return answer
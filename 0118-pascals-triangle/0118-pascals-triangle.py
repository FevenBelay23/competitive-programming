class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        nums=[]
        nums.append([1])
        for i in range(numRows-1):
            new=[1]
            for j in range(i):
                new.append(nums[i][j]+nums[i][j+1])
            new.append(1)
            nums.append(new)
        return nums
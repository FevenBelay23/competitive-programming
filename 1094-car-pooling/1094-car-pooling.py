class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        count=0
        x=-1
        for i in trips:
            x=max(x,i[2])
        arr=[0]*(x+1)
        
        for i in trips:
            pas,start,end=i
            arr[start]+=pas
            arr[end]-=pas
        
        for i in range(x+1):
            count+=arr[i]
            if count>capacity:
                return False
        return True
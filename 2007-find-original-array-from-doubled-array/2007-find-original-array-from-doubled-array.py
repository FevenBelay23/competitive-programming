class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        if len(changed)%2:
            return []
        changed.sort()
        i=0
        j=0
        k=1
        while k<len(changed):
            if changed[k]%2==0:
                while j<k-1 and changed[j]<(changed[k]//2):
                    j+=1
                if changed[j]==(changed[k]//2):
                    changed[i] , changed[j] = changed[j] , changed[i]
                    i+=1
                    j+=1
                    changed[k]=-1
            k+=1  
        if i==len(changed)//2:
            return changed[:i]
        return []
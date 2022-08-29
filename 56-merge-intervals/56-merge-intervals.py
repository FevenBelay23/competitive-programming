class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        non_overlapping=[] 
        intervals.sort()  
        for i in intervals:
            if len(non_overlapping)==0:
                non_overlapping.append(i)
            else:
                j=non_overlapping.pop()
                if j[1]>=i[0]:  
                    non_overlapping.append([j[0],max(j[1],i[1])])
                else:   
                    non_overlapping.append(j)
                    non_overlapping.append(i)
        return non_overlapping
        
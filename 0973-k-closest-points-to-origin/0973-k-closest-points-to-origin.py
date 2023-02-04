class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        closest_pt=[]
        for i in points:
            x=i[0]**2+i[1]**2
            closest_pt.append([x,i])
        closest_pt.sort()
        final = [i[1] for i in closest_pt[:k]]
        return final
        
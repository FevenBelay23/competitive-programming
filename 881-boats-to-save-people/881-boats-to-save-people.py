class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        i = 0
        j= len(people)-1
        k= 0
        while(i <= j):
            if people[i]+people[j] > limit:
                k += 1
                j -= 1
            else:
                i += 1
                j -= 1
                k += 1
        return k
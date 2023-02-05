class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        ans = [0] * (n+1)
        for i in range(len(bookings)):
            start, end = bookings[i][0], bookings[i][1]
            ans [start] += bookings[i][2]
            if end < n:
                ans [end+1] += -bookings[i][2]
        for j in range(1,n+1):
            ans [j] += ans [j-1]
        ans.pop(0)
        return ans 
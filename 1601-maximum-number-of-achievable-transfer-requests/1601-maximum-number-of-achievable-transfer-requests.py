class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        def backtrack(index, count):
            nonlocal max_achievable_request
            if index == len(requests):
                if all(i == 0 for i in request):
                    max_achievable_request = max(max_achievable_request, count)
                return
            From, to = requests[index]
            request[From] -= 1
            request[to] += 1
            backtrack(index + 1, count + 1)
            request[From] += 1
            request[to] -= 1
            backtrack(index + 1, count)
        max_achievable_request = 0
        request = [0] * n
        backtrack(0, 0)
        return max_achievable_request

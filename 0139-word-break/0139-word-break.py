class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        queue = deque([0])
        visited = [False] * len(s)

        while queue:
            start = queue.popleft()
            if not visited[start]:
                for end in range(start + 1, len(s) + 1):
                    if s[start:end] in wordDict:
                        if end == len(s):
                            return True
                        queue.append(end)
                visited[start] = True

        return False
    
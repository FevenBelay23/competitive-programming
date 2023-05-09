class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if "0000" == target:
            return 0
        queue = deque([("0000", 0)])
        visited = set("0000")
        while queue:
            move, temp = queue.popleft()
            for i in range(4):
                for j in [-1, 1]:
                    curr = str((int(move[i]) + j) % 10)
                    new_move = move[:i] + curr + move[i+1:]
                    if new_move not in visited and new_move not in deadends:
                        if new_move == target:
                            return temp + 1
                        queue.append((new_move, temp + 1))
                        visited.add(new_move)
        return -1
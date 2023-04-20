class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        player = [i for i in range(1, n+1)]
        current = 0
        while len(player) > 1:
            current = (current + k - 1) % len(player)
            player.pop(current)
        return player[0]
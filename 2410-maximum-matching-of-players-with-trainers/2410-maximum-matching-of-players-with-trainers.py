class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        play = len(players)
        train = len(trainers)
        i = 0 
        j = 0
        count = 0
        players.sort()
        trainers.sort()
        while i<play and j<train:
            if players[i] <= trainers[j]:
                count += 1
                i +=1
                j += 1
            else:
                j += 1
        return count

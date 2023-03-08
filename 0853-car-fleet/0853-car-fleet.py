class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        car = sorted(zip(position, speed), reverse=True)
        fleets = []
        
        for i in range(n):
            pos, spe = car[i]
            time = (target - pos) / spe
            if not fleets:
                fleets.append(time)
            elif time > fleets[-1]:
                fleets.append(time)
        
        return len(fleets)
        
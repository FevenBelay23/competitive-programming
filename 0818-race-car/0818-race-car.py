class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1)])  
        visited = set([(0, 1)])  
        order = 0  
        while queue:
            for _ in range(len(queue)):
                position, speed = queue.popleft()
                if position == target:
                    return order
                new_position = position + speed
                new_speed = speed * 2
                if (new_position, new_speed) not in visited and 0 < new_position < (target * 2):
                    visited.add((new_position, new_speed))
                    queue.append((new_position, new_speed))
                new_position = position
                new_speed = -1 if speed > 0 else 1
                if (new_position, new_speed) not in visited and 0 < new_position < (target * 2):
                    visited.add((new_position, new_speed))
                    queue.append((new_position, new_speed))
            order += 1
        return -1  

    






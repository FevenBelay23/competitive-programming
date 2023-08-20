class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = collections.defaultdict(list)
        pair = collections.defaultdict(int)
        for i, j in enumerate(recipes):
            for k in ingredients[i]:
                graph[k].append(j)
                pair[j] += 1
        queue = deque(supplies)
        while queue:
            current = queue.popleft()
            while graph[current]:
                j = graph[current].pop()
                if j in pair: 
                    pair[j] -= 1
                if pair[j] == 0:
                    queue.append(j)
        return [i for i in pair if pair[i] == 0]
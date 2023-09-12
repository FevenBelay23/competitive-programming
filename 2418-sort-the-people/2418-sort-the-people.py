class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        n = len(names)
        people = [(names[i], heights[i]) for i in range(n)]
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if people[j][1] < people[j + 1][1] or (people[j][1] == people[j + 1][1] and people[j][0] > people[j + 1][0]):
                    people[j], people[j + 1] = people[j + 1], people[j]
        Sorted = [person[0] for person in people]
        return Sorted

        
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def find(related, x):
            if x not in related:
                related[x] = x
            if related[x] != x:
                related[x] = find(related, related[x])
            return related[x]
        related = {}
        for i in equations:
            x, temp, _, y = i
            if temp == "=":
                if x not in related:
                    related[x] = x
                if y not in related:
                    related[y] = y
        for i in equations:
            x, temp, _, y = i
            if temp == "=":
                first = find(related, x)
                second = find(related, y)
                if first != second:
                    related[first] = second
        for i in equations:
            x, temp, _, y = i
            if temp == "!":
                first = find(related, x)
                second = find(related, y)
                if first == second:
                    return False

        return True

        
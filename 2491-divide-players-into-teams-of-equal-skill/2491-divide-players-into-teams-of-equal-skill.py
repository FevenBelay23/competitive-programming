class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n=len(skill)
        result=0
        skill.sort()
        total=skill[0]+skill[n-1]
        for i in range(n//2):
            if skill[i]+skill[n-1-i]==total:
                result+=(skill[i]*skill[n-1-i])
            else:
                return -1
        return result
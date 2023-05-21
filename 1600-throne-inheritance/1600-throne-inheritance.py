class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.child = {}
        self.die = set()

    def birth(self, parentName: str, childName: str) -> None:
        if parentName in self.child:
            self.child[parentName].append(childName)
        else:
            self.child[parentName] = [childName]

    def death(self, name: str) -> None:
        self.die.add(name)

    def getInheritanceOrder(self) -> List[str]:
        inheritance_order = []
        def dfs(people):
            if people not in self.die:
                inheritance_order.append(people)
            if people in self.child:
                for child in self.child[people]:
                    dfs(child)
        dfs(self.king)
        return inheritance_order


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
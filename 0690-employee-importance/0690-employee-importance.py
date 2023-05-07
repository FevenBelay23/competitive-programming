"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee = {i.id: i for i in employees}
        def dfs(employee_id):
            importance = employee[employee_id].importance
            for subordinate in employee[employee_id].subordinates:
                importance += dfs(subordinate)
            return importance
        return dfs(id)
# Approach:
# 1. Create a hashmap to map employee id to the corresponding employee object for quick lookup.
# 2. Use BFS (queue) starting from the given employee id to traverse all subordinates.
# 3. Add each employee's importance to total_importance and push their subordinates to the queue.

# Time Complexity: O(N) — where N is the number of employees (each employee is processed once)
# Space Complexity: O(N) — for hashmap and queue storage

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
        # Map employee id to employee object
        emp_map = {emp.id: emp for emp in employees}

        total_importance = 0
        queue = deque([id])

        # BFS traversal
        while queue:
            emp_id = queue.popleft()
            employee = emp_map[emp_id]
            total_importance += employee.importance

            # Add all subordinates to the queue
            for sub_id in employee.subordinates:
                queue.append(sub_id)

        return total_importance

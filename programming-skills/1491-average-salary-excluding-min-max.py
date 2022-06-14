class Solution:
    def average(self, salary: List[int]) -> float:
        gross = sum(salary) - min(salary) - max(salary)
        n_employee = len(salary) - 2
        return gross / n_employee
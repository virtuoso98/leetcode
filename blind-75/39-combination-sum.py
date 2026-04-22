class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        candidates.sort()
        def backtrack(curr, target, ptr, accu):
            if curr > target or ptr >= len(candidates):
                return
            if curr == target:
                output.append(accu)
                return
            backtrack(curr + candidates[ptr], target, ptr, accu + [candidates[ptr]])
            backtrack(curr + candidates[ptr], target, ptr + 1, accu + [candidates[ptr]])
            backtrack(curr, target, ptr + 1, accu)
        backtrack(0, target, 0, [])
        return [list(t) for t in {tuple(i) for i in output}]

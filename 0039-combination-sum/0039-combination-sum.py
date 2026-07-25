from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                ans.append(path[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i], path)  
                path.pop()  

        backtrack(0, target, [])
        return ans
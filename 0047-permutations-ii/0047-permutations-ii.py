class Solution:
    def permuteUnique(self, nums):
        nums.sort()
        ans = []
        path = []
        visited = [False] * len(nums)

        def backtrack():
            if len(path) == len(nums):
                ans.append(path[:])
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                # Skip duplicates
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                visited[i] = True
                path.append(nums[i])

                backtrack()

                path.pop()
                visited[i] = False

        backtrack()
        return ans
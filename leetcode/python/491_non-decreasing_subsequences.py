class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        res: list[list[int]] = []
        def dfs(start: int, path: list[int]) -> None:
            if len(path) > 1:
                res.append(path.copy())
            used: set[int] = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                if not path or nums[i] >= path[-1]:
                    path.append(nums[i])
                    used.add(nums[i])
                    dfs(i + 1, path)
                    path.pop()
        dfs(0, [])
        return res
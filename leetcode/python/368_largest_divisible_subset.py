class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        subsets: dict[int, set[int]] = {-1: set()}
        for n in sorted(nums):
            subsets[n] = max([subsets[j] for j in subsets.keys() if n % j == 0], key=len).copy()
            subsets[n].add(n)
        return list(max(subsets.values(), key=len))

s = Solution()
print(s.largestDivisibleSubset([1,2,3]))
print(s.largestDivisibleSubset([1,2,4,8]))
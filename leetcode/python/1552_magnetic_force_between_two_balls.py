class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        position.sort()
        left, right = 1, position[-1] - position[0]
        while left < right:
            mid = (left + right + 1) // 2
            if self.check(position, mid, m):
                left = mid
            else:
                right = mid - 1
        return left

    def check(self, position: list[int], mid: int, m: int):
        count = 1
        pre = position[0]
        for i in range(1, len(position)):
            if position[i] - pre >= mid:
                count += 1
                pre = position[i]
        return count >= m

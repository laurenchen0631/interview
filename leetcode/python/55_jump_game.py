class Solution:
    def canJump(self, nums: list[int]) -> bool:
        visited = set[int]()
        stack: list[int] = [0]
        while stack:
            i = stack.pop()
            visited.add(i)
            n = nums[i]
            if i + n >= len(nums) - 1:
                return True
            for j in range(i+1, i+n+1):
                if j not in visited:
                    stack.append(j)
        return False

    def canJumpDP(nums: list[int]) -> int:
        n = len(nums)
        dp = [-1] * n
        dp[-1] = 1
        for i in range(n - 2, -1, -1):
            furtherest = min(i + nums[i], n - 1)
            for j in range(i+1, furtherest + 1):
                if dp[j] == 1:
                    dp[i] = 1
                    break
        return dp[0] == 1

if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2,3,1,1,4]))
    print(s.canJump([3,2,1,0,4]))
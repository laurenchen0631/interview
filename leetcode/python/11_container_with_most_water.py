class Solution:
    def maxArea(self, height: list[int]) -> int:
        l: int = 0
        r = len(height) - 1
        res: int = 0
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res

    
if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
    # print(s.maxArea([1,1]))
            
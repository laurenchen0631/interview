class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        res: list[int] = []

        curPos: int = 0
        while curPos < len(nums) and nums[curPos] < 0:
            curPos += 1
        curNeg: int = curPos - 1

        while curNeg >= 0 or curPos < len(nums):
            if curPos >= len(nums) or abs(nums[curNeg]) < abs(nums[curPos]):
                res.append(nums[curNeg] ** 2)
                curNeg -= 1
            else:
                res.append(nums[curPos] ** 2)
                curPos += 1
        return res

    def sortedSquaresOpt(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        left = 0
        right = n - 1
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) < abs(nums[right]):
                square = nums[right]
                right -= 1
            else:
                square = nums[left]
                left += 1
            result[i] = square * square
        return result
        
if __name__ == '__main__':
    s = Solution()
    print(s.sortedSquares([-4,-1,0,3,10]))
    print(s.sortedSquares([-7,-3,2,3,11]))
    print(s.sortedSquares([1,2,3,4,5]))
    print(s.sortedSquares([-5, -4, -3, -2, -1]))
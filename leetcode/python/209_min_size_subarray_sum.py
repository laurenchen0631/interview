class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        length: int = 0
        l: int = 0
        sum: int = 0
        for i, n in enumerate(nums):
            sum += n
            while sum >= target and l <= i:
                length = min(i-l+1, length if length > 0 else i-l+1) 
                sum -= nums[l]
                l += 1
        return length

if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2,3,1,2,4,3]))
    print(s.minSubArrayLen(4, [1,4,4]))
    print(s.minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1]))
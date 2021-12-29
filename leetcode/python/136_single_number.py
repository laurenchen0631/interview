class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        k: int = 0
        for n in nums:
            k ^= n
        return k

if __name__ == '__main__':
    s = Solution()
    print(s.singleNumber([4,1,2,1,2]))
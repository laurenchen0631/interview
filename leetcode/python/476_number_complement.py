class Solution:
    def findComplement(self, num: int) -> int:
        return 2 ** len(f'{num:b}') - 1 - num

if __name__ == '__main__':
    s = Solution()
    print(s.findComplement(5))
    print(s.findComplement(1))
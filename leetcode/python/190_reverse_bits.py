class Solution:
    def reverseBits(self, n: int) -> int:
        res: int = 0
        power: int = 31
        while n:
            res += (n&1) << power
            n >>= 1
            power -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.reverseBits(0b00000010100101000001111010011100))
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
            
        res: int = 0
        power: int = 0

        while n > 0:
            if n & 1 == 0:
                res += 2 ** power
            power += 1
            n >>= 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.bitwiseComplement(5))
    print(s.bitwiseComplement(7))
    print(s.bitwiseComplement(10))
    print(s.bitwiseComplement(0))
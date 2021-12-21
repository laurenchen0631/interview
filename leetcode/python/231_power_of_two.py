class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False

        return (n & n-1) == 0

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(-2**31))
    print(s.isPowerOfTwo(0))
    print(s.isPowerOfTwo(1))
    print(s.isPowerOfTwo(2))
    print(s.isPowerOfTwo(15))
    print(s.isPowerOfTwo(17))
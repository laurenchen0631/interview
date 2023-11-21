class Solution:
    def findIntegers(self, n: int) -> int:
        return 1 + self.helper(1, n)
    
    def helper(self, x: int, n: int) -> int:
        if x > n:
            return 0
        
        if x & 1 == 1:
            return 1 + self.helper(x << 1, n)
        else:
            return 1 + self.helper(x << 1, n) + self.helper(x << 1 | 1, n)

    def findIntegersConstant(self, n: int) -> int:
        # f[i] stores the number of valid binary with i bits
        f = [1, 2]
        for i in range(2, 30):
            f.append(f[-1]+f[-2])
        
        # last_seen tells us if there was a one right before. 
        # If that is the case, we are done then and there!
        ans, last_seen = 0, 0
        for i in reversed(range(30)):
            if (1 << i) & n: # is the ith bit set?
                ans += f[i]
                if last_seen: 
                    ans -= 1
                    break
                last_seen = 1
            else:
                last_seen = 0
        return ans+1

s = Solution()
print(s.findIntegers(5))
print(s.findIntegers(10))
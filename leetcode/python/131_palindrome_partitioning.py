class Solution:
    def __init__(self) -> None:
        self.cache: dict[str,str] = {}

    def partition(self, s: str) -> list[list[str]]:
        res: list[list[int]] = []
        if s in self.cache:
            return self.cache[s]
        for i in range(1, len(s) + 1):
            substr = s[:i]
            if not self.isPalindrome(substr):
                continue
                
            if combinations := self.partition(s[i:]):
                for item in combinations:
                    res.append([substr] + item)
            else:
                res.append([substr])
        
        self.cache[s] = res
        return res
    
    def isPalindrome(self, s: str) -> bool:
        for i in range(len(s) // 2):
            if s[i] != s[len(s)-1-i]:
                return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.partition("aab"))
    print(s.partition("a"))
    print(s.partition("abbacb"))
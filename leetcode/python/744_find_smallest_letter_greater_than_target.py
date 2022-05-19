class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if letters[-1] <= target:
            return letters[0]
        
        l = 0
        r = len(letters) - 1
        while l <= r:
            m = (l+r) // 2
            if (m == 0 or letters[m-1] <= target) and letters[m] > target:
                return letters[m]
            elif letters[m] <= target:
                l = m+1
            else:
                r = m-1

s = Solution()
print(s.nextGreatestLetter(letters = ["c","f","j"], target = "a"))
print(s.nextGreatestLetter(letters = ["c","f","j"], target = "c"))
print(s.nextGreatestLetter(letters = ["c","f","j"], target = "d"))
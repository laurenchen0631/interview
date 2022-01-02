from typing import cast


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1: list[str] = []
        s2: list[str] = []
        for c in s:
            if c != '#':
                s1.append(c)
            elif len(s1) > 0:
                s1.pop()
        for c in t:
            if c != '#':
                s2.append(c)
            elif len(s2) > 0:
                s2.pop()
            
        return ''.join(s1) == ''.join(s2)
            
if __name__ == '__main__':
    s = Solution()
    print(s.backspaceCompare("ab#c", "ad#c"))
    print(s.backspaceCompare("ab##", "c#d#"))
    print(s.backspaceCompare("a#c", "b"))
    print(s.backspaceCompare("y#fo##f", "y#f#o##f"))
    

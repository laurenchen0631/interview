class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start: int = 0
        end: int = len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    s = Solution()
    a = ["h","e","l","l","o"]
    s.reverseString(a)
    print(a)

    b =["H","a","n","n","a","h"]
    s.reverseString(b)
    print(b)
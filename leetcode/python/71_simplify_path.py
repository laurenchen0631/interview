class Solution:
    def simplifyPath(self, path: str) -> str:
        dirs = path.split('/')
        stack: list[str] = []
        for d in dirs:
            if d == '..':
                if stack:
                    stack.pop()
            elif not d or d == '.':
                continue
            else:
                stack.append(d)
        return '/' + '/'.join(stack)


s = Solution()
print(s.simplifyPath(path = "/home/"))
print(s.simplifyPath(path = "/../"))
print(s.simplifyPath(path = "/home//foo/"))
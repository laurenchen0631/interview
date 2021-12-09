class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        visited: set[int] = set()
        stack: list[int] = [start]
        while len(stack) > 0:
            i = stack.pop()
            if i in visited:
                continue
            visited.add(i)
            n = arr[i]
            if n == 0:
                return True
            
            if (k := i - n) >= 0:
                stack.append(k)
            if (k := i + n) < len(arr):
                stack.append(k)
        return False

if __name__ == '__main__':
  s = Solution()
  print(s.canReach([4,2,3,0,3,1,2], 5))
  print(s.canReach([4,2,3,0,3,1,2], 0))
  print(s.canReach([3,0,2,1,2], 2))

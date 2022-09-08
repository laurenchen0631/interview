from inspect import stack


class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack: list[int] = []
        for n in asteroids:
            while n < 0 and stack and stack[-1] > 0:
                if stack[-1] < -n:
                    stack.pop()
                    continue
                elif stack[-1] == -n:
                    stack.pop()
                break
            else:
                stack.append(n)
        return stack

s = Solution()
print(s.asteroidCollision([5,10,-5]))
print(s.asteroidCollision([8,-8]))
print(s.asteroidCollision([10, 2,-5]))
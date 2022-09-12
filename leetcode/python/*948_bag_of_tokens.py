from collections import deque


class Solution(object):
    def bagOfTokensScore(self, tokens: list[int], power: int):
        tokens.sort()
        q = deque(tokens)
        ans = cur = 0
        while q and (power >= q[0] or cur):
            while q and power >= q[0]:
                power -= q.popleft()
                cur += 1
            ans = max(ans, cur)

            if q and cur:
                power += q.pop()
                cur -= 1

        return ans
from collections import deque
from this import d


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rCount = senate.count('R')
        dCount = len(senate) - rCount
        bannedR = bannedD = 0
        q = deque(senate)
        while dCount and rCount:
            senator = q.popleft()
            if senator == 'R':
                if bannedR:
                    bannedR -= 1
                    rCount -= 1
                else:
                    bannedD += 1
                    q.append(senator)
            else:
                if bannedD:
                    bannedD -= 1
                    dCount -= 1
                else:
                    bannedR += 1
                    q.append(senator)
        return 'Radiant' if rCount else 'Dire'
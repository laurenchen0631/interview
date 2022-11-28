class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        wins, lost1, loses = set[int](), set[int](), set[int]()
        for winner, loser in matches:
            if winner not in lost1 and winner not in loses:
                wins.add(winner)
            if loser in lost1:
                lost1.remove(loser)
                loses.add(loser)
            elif loser not in loses:
                lost1.add(loser)
                if loser in wins:
                    wins.remove(loser)
        return [sorted(wins), sorted(lost1)]
    
s = Solution()
print(s.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]))
print(s.findWinners([[2,3],[1,3],[5,4],[6,4]]))
class Solution:
    def calPoints(self, ops: list[str]) -> int:
        rounds: list[int] = []
        for op in ops:
            if op == 'C':
                rounds.pop()
            elif op == 'D':
                rounds.append(rounds[-1] * 2)
            elif op == '+':
                rounds.append(rounds[-1] + rounds[-2])
            else:
                rounds.append(int(op))
        return sum(rounds)

s = Solution()
# print(s.calPoints(["5","2","C","D","+"]))
print(s.calPoints(["5","-2","4","C","D","9","+","+"]))
                
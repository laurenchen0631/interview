class Solution:
    def twoCitySchedCost(self, costs: list[list[int]]) -> int:
        # Sort by a gain which company has 
        # by sending a person to city A and not to city B
        costs.sort(key = lambda x : x[0] - x[1])
        print(costs)
        
        total = 0
        n = len(costs) // 2
        # To optimize the company expenses,
        # send the first n persons to the city A
        # and the others to the city B
        for i in range(n):
            total += costs[i][0] + costs[i + n][1]
        return total

s = Solution()
# print(s.twoCitySchedCost([[10,20],[30,200],[400,50],[30,20]]))
# print(s.twoCitySchedCost([[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]))
# print(s.twoCitySchedCost([[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]))
print(s.twoCitySchedCost([[70,311],[74,927],[732,711],[126,583],[857,118],[97,928],[975,843],[175,221],[284,929],[816,602],[689,863],[721,888]]))

# return no. of ways to build a staircase with total n blocks
# Staircase must have at least two steps
# Every step must be strictly decreasing 
def solution(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    dp[2][2] = 1
    for i in range(3, n + 1):
        for j in range(2, i):
            max_next_step = j - 1
            available_blocks = i - j
            dp[i][j] = dp[i][j-1] + dp[available_blocks][min(max_next_step, available_blocks)]
            
        dp[i][i] = dp[i][i - 1] + 1

    return dp[n][n] - 1

# print(solution(3)) # 1
# print(solution(4)) # 1
# print(solution(5)) # 2
# print(solution(6)) # 3
# print(solution(7)) # 4
print(solution(8)) # 5
print(solution(9)) # 7
print(solution(10)) # 9
print(solution(200)) # 487067745
# print(solution(9))
# print(solution(10))


def getUmbrellas(requirement: int, sizes: list[int]):
    dp = [-1] * (requirement + 1)
    dp[0] = 0
    for i in range(1, requirement + 1):
        for size in sizes:
            if size <= i and dp[i - size] != -1:
                if dp[i] == -1:
                    dp[i] = dp[i - size] + 1
                else:
                    dp[i] = min(dp[i], dp[i - size] + 1)
    return dp[requirement]

print(getUmbrellas(5, [3, 5]))
print(getUmbrellas(9, [1, 1, 1, 4, 5, 6]))
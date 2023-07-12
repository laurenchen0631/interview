
def findNumberOfWays(n_intervals, n_processes):
    res = 1
    for _ in range(n_intervals - 1):
        res *= (n_processes - 1)
        res %= 1000000007
        
    return (res * n_processes) % 1000000007
from math import sqrt

def solution(area):
    res = []
    while area > 0:
        size = int(sqrt(area))
        res.append(size * size)
        area -= res[-1]
    return res

print(solution(12))
print(solution(15324))
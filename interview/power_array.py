# find the max product of all the numbers in the array
def solution(xs):
    cur_min = xs[0]
    cur_max = xs[0]
    for n in xs[1:]:
        cur_min, cur_max = min(cur_min, cur_min * n, cur_max * n, n), max(cur_max, cur_min * n, cur_max * n, n)
    return cur_max

# print(solution([2, 0, 2, 2, 0]))
print(solution([-2, -3, 4, -5]))
print(solution([-1, 0, 1]))
        
    
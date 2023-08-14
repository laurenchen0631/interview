
from bisect import bisect_left


def maxMin(operations, x):
    nums = []
    res = []
    for op, v in zip(operations, x):
        if op == 'push':
            i = bisect_left(nums, v)
            nums.insert(i, v)
        else:
            i = bisect_left(nums, v)
            nums.pop(i)
        res.append(nums[-1] * nums[0])
    return res

print(maxMin(['push', 'push', 'push', 'pop'], [1, 2, 3, 1]))
print(maxMin(['push', 'push'], [3,2]))
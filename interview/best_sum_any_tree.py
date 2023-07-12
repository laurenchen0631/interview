#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'bestSumAnyTreePath' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY parent
#  2. INTEGER_ARRAY values
#
from collections import defaultdict
import heapq

def bestSumAnyTreePath(parent, values):
    # Write your code here
    res = values[0]
    tree = defaultdict(list)
    for i, p in enumerate(parent):
        tree[p].append(i)

    def searchMaxPath(node: int) -> int:
        nonlocal res
        if not tree[node]:
            return values[node]
        path_sum = []
        for child in tree[node]:
            heapq.heappush(path_sum, searchMaxPath(child))
            if len(path_sum) > 2:
                heapq.heappop(path_sum)
        
        max_path = path_sum[-1]
        best = max(values[node], max_path + values[node], 0)
        res = max(res, max_path, best)
        if len(path_sum) > 1:
            res = max(res, values[node] + max_path + path_sum[-2])
        return best

    searchMaxPath(0)
    return res

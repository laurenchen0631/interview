# h = 4
#           15
#     7           14
#  3    6     10     13
# 1 2  4 5   8  9  11  12

# h = 5
#                        31
#            15                       30
#     7           14            22           29
#  3    6     10     13     18     21     25     28
# 1 2  4 5   8  9  11  12  16 17  19 20  23 24  26  27

# h is the height of the perfect tree of converters and q is a list of positive integers representing index
def solution(h, q):
    """returns a list of integers p where p[i] is the parent of q[i] in a perfect binary tree of converters"""
    res = []
    for i in q:
        res.append(get_parent(h, i))
    return res

def get_parent(h, i):
    if i == 2**h - 1:
        return -1  # Root node has no parent
    
    parent = 2**h - 1
    for _ in range(h):
        left_child = parent - 2**(h-1)
        right_child = parent - 1

        if i == left_child or i == right_child:
            return parent

        if i < left_child:
            parent = left_child
        else:
            parent = right_child

        h -= 1

print(solution(3, [7, 3, 5, 1]))
print(solution(5, [19, 14, 28]))
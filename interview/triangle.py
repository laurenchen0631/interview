
# 0: if triangle is not valid
# 1: p belongs to the triangle but q does not
# 2: q belongs to the triangle but p does not
# 3: p and q both belong to the triangle
# 4: neither p nor q belongs to the triangle
def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq) -> int:
    if not isTriangleValid(x1, y1, x2, y2, x3, y3):
        return 0

    p_in_triangle = isPointInTriangle(x1, y1, x2, y2, x3, y3, xp, yp)
    q_in_triangle = isPointInTriangle(x1, y1, x2, y2, x3, y3, xq, yq)
    
    if p_in_triangle and q_in_triangle:
        return 3
    elif p_in_triangle:
        return 1
    elif q_in_triangle:
        return 2
    else:
        return 4
    
def isTriangleValid(x1, y1, x2, y2, x3, y3) -> bool:
    print(x1*(y2-y3), x2*(y3-y1), x3*(y1-y2))
    return (x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) != 0

def isPointInTriangle(x1, y1, x2, y2, x3, y3, x, y) -> bool:
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

    b1 = sign((x, y), (x1, y1), (x2, y2)) < 0.0
    b2 = sign((x, y), (x2, y2), (x3, y3)) < 0.0
    b3 = sign((x, y), (x3, y3), (x1, y1)) < 0.0

    return b1 == b2 and b2 == b3
    
print(pointsBelong(0, 0, 4, 0, 2, 2, 1, 1, 2, 0))
print(pointsBelong(0, 0, 1, 1, 2, 2, 1, 1, 2, 0))
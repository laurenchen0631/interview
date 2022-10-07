def add(a: int, b: int) -> int:
    # print((~a&b) + (a&~b) + (a&b))
    print((a&b) + (a|b))
    print((a^b) + (a&b)*2)
    print((~a&b) + (a&~b) + 2*(a&b))

add(1, 2)
add(3, 4)
add(4, 5)
add(-1, 2)
add(8, 8)
add(8, 9)
add(8, 10)
add(32, -4)
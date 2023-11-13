from fractions import Fraction
import math


def solution(matrix: list[list[int]]):
    if len(matrix) == 1:
        return [1, 1]

    prepared = initialize(matrix)
        
    for r in prepared:
        print(r)
        
    prepared = reorganize_zero_rows(prepared)
    
    for r in prepared:
        print(r)
    q, r = get_qr(prepared)
    i = identity(len(q))
    i_q = subtract(i, q)
    f = get_inverse(i_q)
    f_r = multiply(f, r)

    probabilities = normalize_probabilities(f_r[0])

    return probabilities

def lcm(a: int, b: int) -> int:
    return a * b // math.gcd(a, b)

def get_lcd(fractions: list[Fraction]):
    first = fractions[0]
    second = fractions[1]
    _lcd = lcm(first.denominator, second.denominator)

    for i in range(2, len(fractions)):
        _lcd = lcm(_lcd, fractions[i].denominator)

    return _lcd

def normalize_probabilities(fractions):
    lcd = get_lcd(fractions)
    numerators = [lcd * f.numerator // f.denominator  for f in fractions]

    return numerators + [lcd]

def initialize(matrix: list[list[int]]):
    size = len(matrix)
    normalized: list[list] = []

    for row in range(size):
        row_sum = sum(matrix[row])
        
        if row_sum == 0:
            normalized.append(matrix[row])
        else:
            normalized.append([Fraction(matrix[row][column], row_sum) for column in range(size)])
    return normalized

def swap(matrix, i, j):
    s = len(matrix)

    if i == j:
        return matrix

    swapped = []

    for row in range(s):
        new_row = []
        tmp_row = matrix[row]
        if row == i:
            tmp_row = matrix[j]
        if row == j:
            tmp_row = matrix[i]
        for column in range(s):
            temp_el = tmp_row[column]
            if column == i:
                temp_el = tmp_row[j]
            if column == j:
                temp_el = tmp_row[i]
            new_row.append(temp_el)
        swapped.append(new_row)

    return swapped

def reorganize_zero_rows(matrix):
    size = len(matrix)

    zero_row = -1
    for row in range(size):
        row_sum = sum([matrix[row][column] for column in range(size)])

        if row_sum == 0:
            zero_row = row

        if row_sum != 0 and zero_row > -1:
            tmp = swap(matrix, row, zero_row)
            return reorganize_zero_rows(tmp)

    return matrix

def get_transitives_count(matrix):
    non_zero = [
        row for row in range(len(matrix)) if all(
            [matrix[row][column] == 0 for column in range(len(matrix[row]))])
    ]
    return non_zero[0]

def get_qr(matrix):
    transition_count = get_transitives_count(matrix)

    q = [[matrix[row][column] for column in range(transition_count)]
         for row in range(transition_count)]
    r = [[
        matrix[row][column]
        for column in range(transition_count, len(matrix[row]))
    ] for row in range(transition_count)]

    return q, r


def subtract(i, q):
    size = len(i)
    result = [[i[row][column] - q[row][column] for column in range(size)]
              for row in range(size)]
    return result


def identity(size):
    result = [[1 if row == column else 0 for column in range(size)]
              for row in range(size)]
    return result


def get_minor(matrix, i, j):
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def get_determinant(matrix):
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    determinant = 0
    for c in range(len(matrix)):
        determinant += (
            (-1)**c) * matrix[0][c] * get_determinant(get_minor(matrix, 0, c))

    return determinant


def transpose(matrix):
    transposed = [[matrix[row][column] if column== row else matrix[column][row] for column in range(len(matrix[row]))]\
        for row in range(len(matrix))]

    return transposed


def get_inverse(matrix):
    determinant = get_determinant(matrix)

    if len(matrix) == 2:
        return [[matrix[1][1] / determinant, -1 * matrix[0][1] / determinant],
                [-1 * matrix[1][0] / determinant, matrix[0][0] / determinant]]

    cofactors = [[((-1) ** (row + column)) * get_determinant(get_minor(matrix, row, column)) for column in range(len(matrix))]\
                 for row in range(len(matrix))]

    cofactors = transpose(cofactors)

    for row in range(len(cofactors)):
        for column in range(len(cofactors)):
            cofactors[row][column] = cofactors[row][column] / determinant

    return cofactors


def multiply(a, b):
    rows = len(a)
    columns = len(b[0])

    multiplied = [[
        sum([a[row][i] * b[i][column] for i in range(len(a[0]))])
        for column in range(columns)
    ] for row in range(rows)]

    return multiplied


# print(simulate([
#     [0, 1, 1, 1, 0, 0],
#     [1, 0, 1, 0, 1, 0],
#     [1, 1, 0, 1, 0, 1],
#     [1, 0, 1, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0],
# ]))
# Test case

print(solution([
    [0, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 0],
    [1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]))
def transformArray(a, b):
    aArr = sorted(map(int, a.split(' ')))
    bArr = sorted(map(int, b.split(' ')))
    for i in range(len(aArr)):
        if bArr[i] - aArr[i] > 1:
            return False
    return True

print(transformArray('4 2 3 4 0', '1 2 3 4 5'));
# print(transformArray([4,2,3,4,0], [3,3,4,4,0]));
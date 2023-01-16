# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
class ArrayReader(object):
    # Compares the sum of arr[l..r] with the sum of arr[x..y]
    # return 1 if sum(arr[l..r]) > sum(arr[x..y])
    # return 0 if sum(arr[l..r]) == sum(arr[x..y])
    # return -1 if sum(arr[l..r]) < sum(arr[x..y])
    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
        return 0
    # Returns the length of the array
    def length(self) -> int:
        return 0

class Solution:
    def getIndex(self, reader: ArrayReader) -> int:
        l = 0
        r = reader.length() - 1
        while l < r:
            n = (r - l + 2) // 2
            comp  = reader.compareSub(l, l + n - 1, r - n + 1, r)
            if comp == 1:
                r = l + n - 1
            elif comp == -1:
                l = r - n + 1
            else:
                return l + n - 1
        return l
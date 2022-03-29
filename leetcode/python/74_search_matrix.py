class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        row = self.findRow(matrix, target)
        if row == -1:
            return False
        return self.binarySearch(matrix[row], target)

    def findRow(self, mat: list[list[int]], target: int) -> int:
        t, b = 0, len(mat)-1
        while t <= b:
            m = (t + b) // 2
            if mat[m][0] <= target <= mat[m][-1]:
                return m
            if mat[m][-1] < target:
                t = m + 1
            else:
                b = m - 1
        return -1
        
    def binarySearch(self, nums: list[int], target: int) -> bool:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return True
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        return False

    def searchMatrixOpt(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0]) if m else 0
        l = 0
        r = m * n - 1
        while l <= r:
            mid = (l+r) // 2
            (i, j) = divmod(mid, n)
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrixOpt([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(s.searchMatrixOpt([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
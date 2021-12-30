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
        if m == 0:
            return False
        n = len(matrix[0])
        
        # binary search
        left, right = 0, m * n - 1
        while left <= right:
                pivot_idx = (left + right) // 2
                pivot_element = matrix[pivot_idx // n][pivot_idx % n]
                if target == pivot_element:
                    return True
                else:
                    if target < pivot_element:
                        right = pivot_idx - 1
                    else:
                        left = pivot_idx + 1
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))

### You must write an algorithm that runs in O(n) time and without using the division operation.
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        preProduct = [1] * n
        for i in range(1, n):
            preProduct[i] = preProduct[i - 1] * nums[i - 1]

        postProduct = [1] * n
        for i in range(n - 2, -1, -1):
            postProduct[i] = postProduct[i+1] * nums[i + 1]

        return [preProduct[i] * postProduct[i] for i in range(n)]


    def productExceptSelfMinSpace(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        suxAcc = 1
        for i in range(n - 2, -1, -1):
            suxAcc = suxAcc * nums[i+1]
            res[i] *= suxAcc

        return res

if __name__ == '__main__':
    s = Solution()
    print(s.productExceptSelf([1,2,3,4,5]))
    print(s.productExceptSelf([-1,1,0,-3,3]))
    print(s.productExceptSelfMinSpace([1,2,3,4,5]))
    print(s.productExceptSelfMinSpace([-1,1,0,-3,3]))
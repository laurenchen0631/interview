class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        MOD = 10 ** 9 + 7
        stack = []
        res = 0;

        for i in range(len(arr) + 1):
            
            # when i reaches the array length, it is an indication that
            # all the elements have been processed, and the remaining
            # elements in the stack should now be popped out.

            while stack and (i == len(arr) or arr[stack[-1]] >= arr[i]):
                print(stack)

                # Notice the sign ">=", This ensures that no contribution
                # is counted twice. right_boundary takes equal or smaller 
                # elements into account while left_boundary takes only the
                # strictly smaller elements into account

                mid = stack.pop()
                left_boundary = -1 if not stack else stack[-1]
                right_boundary = i

                # count of subarrays where mid is the minimum element
                count = (mid - left_boundary) * (right_boundary - mid)
                res += (count * arr[mid])

            stack.append(i)
        
        return res % MOD

    
s = Solution()
print(s.sumSubarrayMins([3,1,2,4]))
# print(s.sumSubarrayMins([11,81,94,43,3]))
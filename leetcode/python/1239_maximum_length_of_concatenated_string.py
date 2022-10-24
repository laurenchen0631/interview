class Solution:
    def maxLength(self, arr: list[str]) -> int:

        def dfs(i: int, subseq: str) -> int:
            if len(subseq) != len(set(subseq)):
                return 0
            if i == len(arr):
                return len(subseq)

            return max(len(subseq), max([dfs(j+1, subseq+arr[j]) for j in range(i, len(arr))]))
        return dfs(0, '')

s = Solution()
print(s.maxLength(["un","iq","ue"]))
print(s.maxLength(["cha","r","act","ers"]))
print(s.maxLength(["jnfbyktlrqumowxd","mvhgcpxnjzrdei"]))
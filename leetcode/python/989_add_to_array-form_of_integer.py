class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        carry = 0
        for i in range(len(num)-1,-1,-1):
            k, d = divmod(k, 10)
            carry, num[i] = divmod(num[i] + d + carry, 10)
            if k == 0 and carry == 0:
                break
        k += carry
        return num if k == 0 else [int(d) for d in str(k)] + num
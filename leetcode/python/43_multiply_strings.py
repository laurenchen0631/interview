class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        product = [0] * (len(num1) + len(num2))
        for j in range(len(num2)):
            for i in range(len(num1)):
                n, r = divmod(int(num1[-i-1]) * int(num2[-j-1]) +  product[i + j], 10)
                product[i + j] = r
                product[i + j + 1] += n

        while product and product[-1] == 0:
            product.pop()
        product.reverse()
        return ''.join(map(str, product)) if product else '0'
                
s = Solution()
print(s.multiply("123", "456"))
print(s.multiply("0", "0"))
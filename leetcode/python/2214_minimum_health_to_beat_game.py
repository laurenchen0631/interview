class Solution:
    def minimumHealth(self, damage: list[int], armor: int) -> int:
        maxDamage = 0
        total = 0
        for d in damage:
            total += d
            maxDamage = max(maxDamage, d)
        return total - maxDamage + max(maxDamage - armor, 0) + 1
    
s = Solution()
print(s.minimumHealth(damage = [2,7,4,3], armor = 4))
print(s.minimumHealth(damage = [2,5,3,4], armor = 7))
print(s.minimumHealth(damage = [3,3,3], armor = 0))
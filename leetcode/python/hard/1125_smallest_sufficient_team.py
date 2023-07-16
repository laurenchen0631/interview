class Solution:
    def smallestSufficientTeam(self, req_skills: list[str], people: list[list[str]]) -> list[int]:
        m, n = len(req_skills), len(people)
        skill_id = {v: i for i, v in enumerate(req_skills)}
        skills_mask = [0] * n
        for i, p in enumerate(people):
            for s in p:
                skills_mask[i] |= 1 << skill_id[s]
        dp = [(1 << n) - 1] * (1 << m)
        dp[0] = 0
        for mask in range(1, 1 << m):
            for i in range(n):
                prev_skill = mask & ~skills_mask[i] 
                if prev_skill == mask:
                    continue
                people_mask = dp[prev_skill] | (1 << i)
                if people_mask.bit_count() < dp[mask].bit_count():
                    dp[mask] = people_mask
        
        res = []
        for i in range(n):
            if dp[-1] & (1 << i):
                res.append(i)
        return res
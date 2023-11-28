class Solution:
    # SSPPSPSPPSPPPS
    # SS | PPSPSPPSPPPS
    #     > PPSPS | PPSPPPS
    # 
    # SSP | PSPSPPSPPPS
    # sSPP | SPSPPSPPPS
    def numberOfWays(self, corridor: str) -> int:
        MOD = 10 ** 9 + 7

        pos = []
        # [0, 1, 4, 6]
        for i, c in enumerate(corridor):
            if c == 'S':
                pos.append(i)
        
        if len(pos) % 2 != 0 or len(pos) == 0:
            return 0
        
        res = 1
        prev = pos[1]
        for i in range(2, len(pos), 2):
            res = (res * (pos[i] - prev)) % MOD
            prev = pos[i+1]
        return res
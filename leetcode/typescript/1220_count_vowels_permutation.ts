
// WAYS(n, c) means #ways to compose string ending with c
// a -> e | e -> a, i | i -> a,e,o,u | o -> i,u | u -> a
// dp[0] => a, dp[1] => e, dp[2] => i, dp[3] => o, dp[4] => u
// dp[0] = dp[1] + dp[2] + d[4]
// dp[1] = dp[0] + dp[2]
// dp[2] = dp[1] + dp[3]
// dp[3] = dp[2]
// dp[4] = dp[2] + dp[3]
function countVowelPermutation(n: number): number {
    let dp = new Array<number>(5).fill(1);
    const mod = 1e9 + 7;
    for (let i = 1; i < n; i++) {
        const newDP = [
            (dp[1] + dp[2] + dp[4]) % mod,
            (dp[0] + dp[2]) % mod,
            (dp[1] + dp[3]) % mod,
            dp[2],
            (dp[2] + dp[3]) % mod,
        ]
        dp = newDP;
    }

    return dp.reduce((acc, v) => (acc + v) % mod, 0);

};
function numFactoredBinaryTrees(arr: number[]): number {
    arr.sort((a, b) => a - b);
    const index = new Map<number, number>();
    for (let i = 0; i < arr.length; i++) {
        index.set(arr[i], i);
    }
    const dp = new Array(arr.length).fill(1);
    for (const [i, n] of arr.entries()) {
        const upper = Math.sqrt(n);
        for (let l = 0; arr[l] <= upper; l++) {
            const rem = n % arr[l];
            const r = index.get(n / arr[l]);
            if (rem === 0 && r !== undefined) {
                dp[i] += dp[l] * dp[r];
                if (arr[r] !== arr[l]) {
                    dp[i] += dp[l] * dp[r];
                }
                dp[i] %= (10 ** 9 + 7);
            }
            
        }
    }

    return dp.reduce((a, b) => (a + b) % (10 ** 9 + 7), 0);
};
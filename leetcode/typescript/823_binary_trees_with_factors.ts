function numFactoredBinaryTrees(arr: number[]): number {
    arr.sort((a, b) => a - b);
    const index = new Map<number, number>();
    for (let i = 0; i < arr.length; i++) {
        index.set(arr[i], i);
    }
    const dp = new Array(arr.length).fill(1);
    for (const [i, n] of arr.entries()) {
        const upper = Math.sqrt(n);
        for (let j = 0; arr[j] <= upper; j++) {
            const rem = n % arr[j];
            const k = n / arr[j];
            if (rem === 0 && index.has(k)) {
                dp[i] += dp[j] * dp[index.get(k)!];
                if (k !== arr[j]) {
                    dp[i] += dp[j] * dp[index.get(k)!];
                }
                dp[i] %= (10 ** 9 + 7);
            }
            
        }
    }

    return dp.reduce((a, b) => a + b, 0) % (10 ** 9 + 7);
};
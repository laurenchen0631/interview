//   b a b a d
// b 1 x x x 1
// a   1 x 1 x
// b.    1 x x
// a.      1 x
// d.        1

function longestPalindrome(s: string): string {
    let res = s[0];
    const n = s.length;
    const dp: boolean[][] = [];
    for (let i = 0; i < n; i++) {
        dp.push(new Array<boolean>(n).fill(false));
        dp[i][i] = true;
    }

    for (let i = n - 2; i >= 0; i--) {
        for (let j = i+1; j < n; j++) {
            if (s[i] != s[j]) continue;

            if (j - i === 1 || dp[i+1][j-1]) {
                dp[i][j] = true;
                if (res.length < j - i + 1) {
                    res = s.slice(i, j+1);
                }
            }
        }
    }
    return res;



};
function minOperations(nums: number[]): number {
    const n = nums.length;
    const sortedNums = Array.from(new Set(nums)).sort((a, b) => a - b);
    let res = n;

    for (const [i, l] of sortedNums.entries()) {
        const r = l + n - 1;
        let j = i;
        bisectRight(sortedNums, r);
        const count = j - i;
        res = Math.min(res, n - count);
    }
    return res;
};

function bisectRight(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length;

    while (left < right) {
        const mid = Math.floor((left + right) / 2);

        if (nums[mid] > target) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return left;
}

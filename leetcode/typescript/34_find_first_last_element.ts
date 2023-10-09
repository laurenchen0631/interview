function searchRange(nums: number[], target: number): [number, number] {
    const l = bisectLeft(nums, target)
    if (l === -1) return [-1, -1];
    return [l, bisectRight(nums, target)]
};

function bisectLeft(nums: number[], target: number): number {
    let l = 0;
    let r = nums.length - 1;
    while (l < r) {
        const m = Math.floor((l + r) / 2);
        if (nums[m] >= target) {
            r = m
        }
        else{
            l = m + 1
        }
    }
    return nums[l] === target ? l : -1;
}

function bisectRight(nums: number[], target: number): number {
    let l = 0;
    let r = nums.length - 1;
    while (l < r) {
        const m = Math.floor((l + r + 1) / 2);
        if (nums[m] <= target) {
            l = m
        }
        else{
            r = m - 1
        }
    }
    return nums[l] === target ? l : -1;
}
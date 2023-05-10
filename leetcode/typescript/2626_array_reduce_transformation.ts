type Fn = (accum: number, curr: number) => number

function reduce(nums: number[], fn: Fn, init: number): number {
    let accum: number = init;
    for (const curr of nums) {
        accum = fn(accum, curr);
    }
    return accum;
};
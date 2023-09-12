
// MEX is the smallest non-negative integer that is not present in the array A.
// For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

// [0, 1, 2, 2, 0, 0, 10, 3], x = 3
// [0, 1, 2, 5, 3, 6, 4, 3] => 7
function getMaxMex(arr, x) {
    const baseCount = new Map();
    for (const n of arr) {
        const k = n % x;
        baseCount.set(k, (baseCount.get(k) || 0) + 1);
    }

    for (let i = 0; i < arr.length; i += 1) {
        const base = i % x;
        if ((baseCount.get(base) || 0) === 0) {
            return i;
        }
        baseCount.set(base, baseCount.get(base) - 1);
    }
    return arr.length;
}

// console.log(getMaxMex([0, 1, 2, 2, 0, 0, 10, 3], 3));
// console.log(getMaxMex([1,3,4], 2));
// console.log(getMaxMex([0,1,2,1,3], 3));
console.log(getMaxMex([1,1,1,1], 2));
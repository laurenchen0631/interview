type MultiDimensionalArray = (number | MultiDimensionalArray)[];

function flat(arr:  MultiDimensionalArray, n: number): MultiDimensionalArray {
    const result: MultiDimensionalArray = [];
    for (const item of arr) {
        if (Array.isArray(item) && n > 0) {
            result.push(...flat(item, n - 1));
        } else {
            result.push(item);
        }
    }
    return result;
};
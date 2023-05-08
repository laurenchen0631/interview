function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const res: number[] = [];
    for (let [i, n] of arr.entries()) {
        res.push(fn(n, i));
    }
    return res;
    
};
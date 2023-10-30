function sortByBits(arr: number[]): number[] {
    arr.sort((a, b) => {
        const b1 = a.toString(2).match(/1/g)?.length ?? 0;
        const b2 = b.toString(2).match(/1/g)?.length ?? 0;

        if (b1 !== b2) {
            return b1 - b2;
        }
        else {
            return a - b;
        }
    });

    return arr;
};
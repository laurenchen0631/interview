declare global {
    interface Array<T> {
        groupBy(fn: (item: T) => string): Record<string, T[]>
    }
}

Array.prototype.groupBy = function<T>(fn) {
    const record: Record<string, T[]> = {}
    this.forEach(item => {
        const key = fn(item);
        if (!record[key]) {
            record[key] = [];
        }
        record[key].push(item);
    });
    return record;
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
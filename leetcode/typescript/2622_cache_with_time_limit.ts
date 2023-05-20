class TimeLimitedCache {
    timeMap: Map<number, [number, any]>;

    constructor() {
        this.timeMap = new Map();
    }

    set(key: number, value: number, duration: number): boolean {
        const existed = this.timeMap.has(key);
        if (existed) {
            clearTimeout(this.timeMap.get(key)?.[1]);
        }

        const timer = setTimeout(() => {
            this.timeMap.delete(key);
        }, duration);
        this.timeMap.set(key, [value, timer]);
        return existed;
    }

    get(key: number): number {
        if (this.timeMap.has(key)) {
            return this.timeMap.get(key)?.[0] ?? -1;
        }
        return -1;
    }

	count(): number {
        return this.timeMap.size;
    }
}

/**
 * Your TimeLimitedCache object will be instantiated and called as such:
 * var obj = new TimeLimitedCache()
 * obj.set(1, 42, 1000); // false
 * obj.get(1) // 42
 * obj.count() // 1
 */
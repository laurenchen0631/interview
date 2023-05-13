type Fn = (...params: any) => any

function memoize(fn: Fn): Fn {
    const cache = new Map()
    return function(...args) {
        const key = JSON.stringify(args)
        if (cache.has(key)) {
            return cache.get(key)
        }
        const result = fn(...args)
        cache.set(key, result)
        return result
    }
}
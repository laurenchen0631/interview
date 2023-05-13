function once<T extends (...args: any[]) => any>(fn: T):
    (...args: Parameters<T>) => ReturnType<T> | undefined
{
    let used = false
    return function (...args) {
        if (!used) {
            used = true
            return fn(...args)
        }
    };
}
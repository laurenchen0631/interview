function createCounter(n: number): () => number {
    let counter = n;
    return function() {
        return counter++;
    }
}

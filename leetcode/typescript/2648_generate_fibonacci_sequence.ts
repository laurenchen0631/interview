function* fibGenerator(): Generator<number, any, number> {
    let x = 0;
    yield x;
    let y = 1;
    yield y;
    while (true) {
        const z = x + y;
        yield z;
        [x, y] = [y, z];
    }
};

/**
 * const gen = fibGenerator();
 * gen.next().value; // 0
 * gen.next().value; // 1
 */
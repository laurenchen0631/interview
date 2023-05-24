function jsonToMatrix(arr: any[]): (string | number | boolean | null)[][] {
    const keys = arr.reduce<Set<string>>((acc, cur) => {
        getKeys(cur).forEach(key => acc.add(key));
        return acc;
    }, new Set<string>());
    const sortedKeys = Array.from(keys).sort();

    const mat: (string | number | boolean | null)[][] = [sortedKeys];
    arr.forEach(obj => {
        mat.push(sortedKeys.map(key => getValue(obj, key)));
    });
    return mat;
};

function isObject(obj: any): boolean {
    return typeof obj === 'object' && obj !== null;
}

function getKeys(obj: object): string[] {
    if (!isObject(obj)) return [''];
    return Object.keys(obj).reduce<string[]>(
        (acc, cur) => {
            const keys = getKeys(obj[cur]).map(key => key ? `${cur}.${key}` : cur);
            acc.push(...keys);
            return acc;
        }, 
        []
    );
}

function getValue(obj: object, path: string): any {
    const paths = path.split('.');
    let i = 0;
    let value = obj;
    while (i < paths.length) {
        if (!isObject(value)) break;
        value = value[paths[i]];
        i++;
    }

    if (i < paths.length || isObject(value) || value === undefined)
        return ''
    return value;
}
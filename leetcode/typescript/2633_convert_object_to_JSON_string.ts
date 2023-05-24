function jsonStringify(object: any): string {
    if (object === null) return 'null';
    if (typeof object === 'string') return `"${object}"`;
    if (typeof object !== 'object') return String(object);

    const items: string[] = []
    if (Array.isArray(object)) {
        for (const v of object) {
            items.push(jsonStringify(v));
        }
        return `[${items.join(',')}]`;
    }

    for (let key in object) {
        items.push(`"${key}":${jsonStringify(object[key])}`);
    }
    return `{${items.join(',')}}`;
};
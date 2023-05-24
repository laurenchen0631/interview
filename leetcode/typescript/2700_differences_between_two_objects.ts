function objDiff(obj1: object | any[], obj2: object | any[]): object {
    const diff = {};
    for (const key in obj1) {
        if (!obj2.hasOwnProperty(key)) continue;

        if ((typeof obj1[key] !== 'object' || obj1[key] === null) && obj1[key] !== obj2[key]) {
            diff[key] = [obj1[key], obj2[key]];
        }
        else if (
            (Array.isArray(obj1[key]) && !Array.isArray(obj2[key])) ||
            (Array.isArray(obj2[key]) && !Array.isArray(obj1[key]))
        ) {
            diff[key] = [obj1[key], obj2[key]];
        }
        else if (Array.isArray(obj1[key]) && Array.isArray(obj2[key])) {
            const subDiff = objDiff(obj1[key], obj2[key]);
            if (Object.keys(subDiff).length > 0) {
                diff[key] = subDiff;
            }
        }
        else if (typeof obj1[key] === 'object' && typeof obj2[key] === 'object') {
            const subDiff = objDiff(obj1[key], obj2[key]);
            if (Object.keys(subDiff).length > 0) {
                diff[key] = subDiff;
            }
        }
    }
    return diff;
};
function areDeeplyEqual(o1: any, o2: any): boolean {
    if (o1 === o2) return true;
    if (typeof o1 !== "object" || typeof o2 !== "object") return false;
    if (Object.keys(o1).length !== Object.keys(o2).length) return false;

    // check array
    if (Array.isArray(o1) !== Array.isArray(o2)) return false;


    for (let key in o1) {
        if (!o2.hasOwnProperty(key)) return false;

        if (typeof o1[key] === "object" && typeof o2[key] === "object") {
            if (!areDeeplyEqual(o1[key], o2[key])) 
                return false;
        }
        else if (o1[key] !== o2[key]) 
            return false;
    }
    return true;
};

const o1 = {a: 1, b: 2, c: {d: 3, e: 4}};
const o2 = {a: 1, b: 2, c: {d: 3, e: 4}};

console.log(areDeeplyEqual(o1, o2)); // true
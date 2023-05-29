function checkIfInstanceOf(obj: any, classFunction: any): boolean {
    if (obj === null || obj === undefined || typeof classFunction !== 'function') {
        return false;
    }

    if (typeof obj !== 'object') {
        obj = Object(obj);
    }

    return obj instanceof classFunction;
};

/**
 * checkIfInstanceOf(new Date(), Date); // true
 */
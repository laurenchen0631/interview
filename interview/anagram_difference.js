
// all string are lowercase
function getMinimumDifference(a, b) {
    // a is array of strings
    // b is array of strings
    const ans = [];
    for (let i = 0; i < a.length; i += 1) {
        if (a[i].length !== b[i].length) {
            ans.push(-1);
            continue;
        }
        ans.push(getMinModification(a[i], b[i]));
    }

    return ans;
}

function getMinModification(a, b) {
    const aMap = countChars(a);
    const bMap = countChars(b);
    let res = 0;

    // get minimum difference
    for (const [ch, count] of aMap) {
        const bCount = bMap.get(ch) || 0;
        if (count > bCount) {
            res += count - bCount;
        }
    }

    for (const [ch, count] of bMap) {
        const aCount = aMap.get(ch) || 0;
        if (count > aCount) {
            res += count - aCount;
        }
    }
    return res / 2;
}

function countChars(str) {
    const res = new Map();
    for (const ch of str) {
        res.set(ch, (res.get(ch) || 0) + 1);
    }
    return res;
}

getMinimumDifference(
    ['a', 'jk', 'abb', 'mn', 'abc'], 
    ['bb', 'kj', 'bbc', 'op', 'def']
);

getMinimumDifference(
    ['tea', 'tea', 'act'],
    ['ate', 'toe', 'acts'] 
);

getMinimumDifference(
    ['abc', 'aaa'],
    ['bba', 'abc']
);    
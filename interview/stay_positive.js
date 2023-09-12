

function minStart(arr) {
    // Write your code here
    let res = 0;
    let curSum = 0;
    for (const n of arr) {
        curSum += n;
        if (curSum < 1) {
            res += 1 - curSum;
            curSum = 1;
        }
    }
    return res == 0 ? 1 : res;
}

console.log(minStart([-4,3,2,1]))
console.log(minStart([3,-6,5,-2,1]))
console.log(minStart([-5,4,-2,3,1]))
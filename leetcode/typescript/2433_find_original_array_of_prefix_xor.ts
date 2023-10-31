function findArray(pref: number[]): number[] {
    const res: number[] = [pref[0]];
    for (let i = 1; i < pref.length; i++) {
        res.push(pref[i] ^ pref[i-1]);
    }
    return res;
};

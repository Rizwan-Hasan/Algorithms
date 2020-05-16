function maxSubarray(arr) {
    let mx = Number.MAX_SAFE_INTEGER * -1;
    let val = mx;
    for (let i in arr) {
        val = Math.max(i, i + val);
        if (val > mx) {
            mx = val;
        }
    }
    return mx;
}

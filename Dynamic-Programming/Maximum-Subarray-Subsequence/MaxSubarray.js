var maxSubArrayKadane = function (A) {
    let mx = Number.MAX_SAFE_INTEGER * -1;
    let val = mx;
    for (let i = 0; i < A.length; i += 1) {
        val = Math.max(A[i], A[i] + val);
        if (val > mx) {
            mx = val;
        }
    }
    return mx;
};
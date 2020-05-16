/**
 * @param {number[]} A
 * @return {number}
 */

var maxSubarraySumCircular = function (A) {
    let k = maxSubArrayKadane(A);
    let CS = 0;
    for (let i = 0; i < A.length; i += 1) {
        CS += A[i];
        A[i] = A[i] * -1;
    }
    CS += maxSubArrayKadane(A);
    if (CS > k && CS != 0) {
        return CS;
    } else {
        return k;
    }
};

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

import sys


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        k = self.__maxSubArrayKadane(A)

        CS: int = 0
        for i in range(len(A)):
            CS += A[i]
            A[i] = A[i] * -1

        CS += self.__maxSubArrayKadane(A)

        return CS if CS > k and CS != 0 else k

    def __maxSubArrayKadane(self, nums: list):
        mx = val = sys.maxsize * -1
        for i in nums:
            val = max(i, i + val)
            if val > mx:
                mx = val
        return mx
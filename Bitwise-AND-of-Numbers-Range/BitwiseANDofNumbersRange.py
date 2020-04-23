class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        numOfRightShift: int = 0
        while m < n:
            m >>= 1
            n >>= 1
            numOfRightShift += 1
        else:
            return m << numOfRightShift
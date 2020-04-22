from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumDict: Dict[int, bool] = {0: 1}
        s: int = 0
        count: int = 0
        for i in nums:
            s += i
            if s - k in sumDict:
                count += sumDict[s - k]
            if s in sumDict:
                sumDict[s] += 1
            else:
                sumDict[s] = 1
        return count

def main():
    print(Solution().subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))

if __name__ == '__main__':
    main()

from typing import List, Tuple, Dict, Set

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        matrix = [[None for _ in range(m)] for _ in range(n)]
        matrix[0][0] = grid[0][0]
        for i in range(1, max(n, m)):
            try:
                matrix[0][i] = matrix[0][i - 1] + grid[0][i]
            except IndexError:
                pass
            try:
                matrix[i][0] = matrix[i - 1][0] + grid[i][0]
            except IndexError:
                pass

        for row in range(1, n):
            for col in range(1, m):
                matrix[row][col] = min(matrix[row - 1][col],
                                       matrix[row][col - 1]) + grid[row][col]

        return matrix[n - 1][m - 1]

def main():
    # print(Solution().minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
    print(Solution().minPathSum([[1, 3, 5, 8], [4, 2, 1, 7], [4, 3, 2, 3]]))

if __name__ == '__main__':
    main()

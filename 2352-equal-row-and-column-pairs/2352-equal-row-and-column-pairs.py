class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:

        f = {}

        # store frequency of each row
        for row in grid:
            row = tuple(row)
            f[row] = f.get(row, 0) + 1

        ans = 0
        n = len(grid)

        # create each column
        for j in range(n):
            col = []

            for i in range(n):
                col.append(grid[i][j])

            col = tuple(col)

            if col in f:
                ans += f[col]

        return ans
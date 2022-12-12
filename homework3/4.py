class Solution:
    @staticmethod
    def numIslands(grid):
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    Solution.bfs(grid, i, j)
        return count

    @staticmethod
    def bfs(grid, i, j):
        if i < 0 or i >= len(grid): return
        if j < 0 or j >= len(grid[0]): return
        if grid[i][j] == "0": return

        grid[i][j] = "0"
        Solution.bfs(grid, i + 1, j)
        Solution.bfs(grid, i - 1, j)
        Solution.bfs(grid, i, j + 1)
        Solution.bfs(grid, i, j - 1)


def main():
    matrix = [
              ["1","1","0","0","0"],
              ["1","1","0","0","0"],
              ["0","0","1","0","0"],
              ["0","0","0","1","1"]
            ]
    print(Solution.numIslands(matrix))

main()
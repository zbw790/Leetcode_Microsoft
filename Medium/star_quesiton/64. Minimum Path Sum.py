class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 这个题就是用dp的方法修改原matrix的值，因为每个点只能从左边或者上边过来，所以每个点的值就是左边和上边的值的最小值加上当前点的值
        # 空间复杂度是O(1)，时间复杂度是O(m*n)  
        m = len(grid)
        n = len(grid[0])

        acc = 0
        for x in range(n):
            acc = grid[0][x] + acc
            grid[0][x] = acc

        acc = 0
        for y in range(m):
            acc = grid[y][0] + acc
            grid[y][0] = acc

        for x in range(1, n):
            for y in range(1, m):
                grid[y][x] = min(grid[y - 1][x], grid[y][x - 1]) + grid[y][x]
        
        return grid[m - 1][n - 1]

        # 还有一种方法是用一个dp matrix来做，空间复杂度是O(m*n)，时间复杂度是O(m*n)
        # m = len(grid)
        # n = len(grid[0])
        # pd_matrix = [[0] * n for _ in range(m)]

        # for x in range(n):
        #     for y in range(m):
        #         pd_matrix[y][x] = grid[y][x]

        # acc = 0
        # for y in range(len(pd_matrix)):
        #     acc = pd_matrix[y][0] + acc
        #     pd_matrix[y][0] = acc
        
        # acc = 0
        # for x in range(len(pd_matrix[0])):
        #     acc = pd_matrix[0][x] + acc
        #     pd_matrix[0][x] = acc
        
        # for x in range(1, n):
        #     for y in range(1, m):
        #         pd_matrix[y][x] = min(pd_matrix[y - 1][x], pd_matrix[y][x - 1]) + pd_matrix[y][x]
        
        # return pd_matrix[m - 1][n - 1]

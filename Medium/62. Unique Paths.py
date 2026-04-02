class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 第一横排和第一竖排的path number都是1，因为只能往右或者往下走
        dp_matrix = [[0]* n for _ in range(m)]

        for x in range(len(dp_matrix[0])):
            dp_matrix[0][x] = 1
        
        for y in range(len(dp_matrix)):
            dp_matrix[y][0] = 1

        for y in range(1, len(dp_matrix)):
            for x in range(1, len(dp_matrix[y])):
                dp_matrix[y][x] = dp_matrix[y - 1][x] + dp_matrix[y][x - 1]
        
        return dp_matrix[m-1][n-1]

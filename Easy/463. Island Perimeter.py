class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total_perimeter = 0
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == 1:
                    total_perimeter += self.calculate_perimeter(grid, x, y)
        
        return total_perimeter

    def calculate_perimeter(self, grid, x, y):
        perimeter = 0
        if x - 1 < 0 or grid[x - 1][y] != 1:
            perimeter += 1
        if x + 1 >= len(grid) or grid[x + 1][y] != 1:
            perimeter += 1
        if y - 1 < 0 or grid[x][y - 1] != 1:
            perimeter += 1
        if y + 1 >= len(grid[x]) or grid[x][y + 1] != 1:
            perimeter += 1
        return perimeter
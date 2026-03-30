class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]

        for i in range (2, numRows):
            temp_arr = []
            temp_arr.append(1)
            for x in range(1, len(result[i - 1])):
                temp_arr.append(result[i - 1][x] + result[i - 1][x - 1])
            temp_arr.append(1)
            result.append(temp_arr)
        
        return result

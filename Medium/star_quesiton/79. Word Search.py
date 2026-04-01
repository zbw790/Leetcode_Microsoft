class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #因为不能回到之前的位置，所以需要一个set跟踪
        #要两层嵌套，第一层遍历全部字母找到开头，第二层负责后续的字母，只需要遍历当前字母周围的四个字母 
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True
        return False

    def backtrack(self, row, col, suffix):
        if len(suffix) == 0:
            return True

        if(row < 0 or row == self.ROWS or col < 0 or col == self.COLS or self.board[row][col] != suffix[0]):
            return False
        
        ret = False

        self.board[row][col] = "#"
        for rowOffset, colOffset in [(0,1), (1,0), (0,-1), (-1,0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, suffix[1:])
            if ret:
                break
        
        self.board[row][col] = suffix[0]

        return ret


        coordinate_set = set()

        def back_track(m, n, index, coordinate_set):
            if board[m][n] == word[index] and index == len(word) - 1 and (m,n) not in coordinate_set:
                return True
                
            if index >= len(word) or board[m][n] != word[index] or (m,n) in coordinate_set:
                return False
            
            coordinate_set.add((m, n))

            result = False

            if m + 1 < len(board):
                if back_track(m + 1, n, index + 1, coordinate_set):
                    result = True
            if m - 1 >= 0 and result is False:
                if back_track(m - 1, n, index + 1, coordinate_set):
                    result = True
            if n + 1 < len(board[m]) and result is False:
                if back_track(m, n + 1, index + 1, coordinate_set):
                    result = True
            if n - 1 >= 0 and result is False:
                if back_track(m, n - 1, index + 1, coordinate_set):
                    result = True
            
            if result is False:
                coordinate_set.remove((m, n))
                return False
            
            return True

        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == word[0]:
                    if back_track(x, y, 0, coordinate_set):
                        return True
        
        return False


#我自己的第一次解法，有点拉垮，时间上也不是最优
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #因为不能回到之前的位置，所以需要一个set跟踪
        #要两层嵌套，第一层遍历全部字母找到开头，第二层负责后续的字母，只需要遍历当前字母周围的四个字母
        coordinate_set = set()

        def back_track(m, n, index, coordinate_set):
            if board[m][n] == word[index] and index == len(word) - 1 and (m,n) not in coordinate_set:
                return True
                
            if index >= len(word) or board[m][n] != word[index] or (m,n) in coordinate_set:
                return False
            
            coordinate_set.add((m, n))

            result = False

            if m + 1 < len(board):
                if back_track(m + 1, n, index + 1, coordinate_set):
                    result = True
            if m - 1 >= 0 and result is False:
                if back_track(m - 1, n, index + 1, coordinate_set):
                    result = True
            if n + 1 < len(board[m]) and result is False:
                if back_track(m, n + 1, index + 1, coordinate_set):
                    result = True
            if n - 1 >= 0 and result is False:
                if back_track(m, n - 1, index + 1, coordinate_set):
                    result = True
            
            if result is False:
                coordinate_set.remove((m, n))
                return False
            
            return True

        for x in range(len(board)):
            for y in range(len(board[x])):
                if board[x][y] == word[0]:
                    if back_track(x, y, 0, coordinate_set):
                        return True
        
        return False

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp 算法
        dp_matrix = [[False] * len(s) for _ in range(len(s))]

        start = 0
        max_len = 1

        for i in range(len(s)):
            dp_matrix[i][i] = True
        
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                dp_matrix[i][i + 1] = True
                start = i
                max_len = 2
        
        for j in range(2, len(s)):
            for i in range(len(s) - j):
                if s[i] == s[i + j] and dp_matrix[i+1][i + j - 1] == True:
                    dp_matrix[i][i + j] = True
                    if j + 1 > max_len:
                        start = i
                        max_len = j + 1
        return s[start:start + max_len]

            
        # 中心扩展算法，这个简单
        if len(s) <= 1:
            return s
    
        def expand(left, right):
            nonlocal max_substring
            if right >= len(s) or left < 0:
                return 
            
            while s[left] == s[right]:
                if left - 1 >= 0 and right + 1 < len(s):
                    left -= 1
                    right += 1
                else:
                    break

            if s[left] != s[right]:
                left += 1
                right -= 1
            
            if len(s[left: right + 1]) > len(max_substring):
                max_substring = s[left: right + 1]

        max_substring = ""
        for i in range(len(s)):
            expand(i, i)
            expand(i, i+1)
        return max_substring
        
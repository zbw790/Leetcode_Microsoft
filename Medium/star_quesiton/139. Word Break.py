class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        word_set = set(wordDict)

        m = len(s)

        dp_matrix = [False] * (m + 1)
        dp_matrix[0] = True

        for i in range(1, m + 1):
            for j in range(i):
                if dp_matrix[j] is True and s[j:i] in word_set:
                    dp_matrix[i] = True
                    break
        
        return dp_matrix[-1]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
            
        dp_list = [0] * (n + 1)
        dp_list[1] = 1
        dp_list[2] = 2

        for i in range(3, n + 1):
            dp_list[i] = dp_list[i - 1] + dp_list[i - 2]

        return dp_list[n]
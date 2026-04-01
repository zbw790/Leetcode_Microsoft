class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #回溯的本质就是DPS，把每一个选择都暴力破解了就行
        final_combinations = []
        choices = ["(", ")"]

        def back_track(o, c, parantheses_list):
            if o == c and c == n:
                final_combinations.append("".join(parantheses_list))
                return None
            elif c > o or c > n or o > n:
                return None
            
            for choice in choices:
                parantheses_list.append(choice)
                if choice == "(":
                    back_track(o + 1, c, parantheses_list)
                else:
                    back_track(o, c + 1, parantheses_list)
                parantheses_list.pop()
        
        back_track(0, 0, [])
        return final_combinations
                

            


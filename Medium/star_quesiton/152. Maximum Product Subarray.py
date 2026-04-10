class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = nums[0]
        cur_min = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            # 三个候选值：重新开始、延续最大、延续最小
            candidates = (nums[i], cur_max * nums[i], cur_min * nums[i])
            cur_max = max(candidates)
            cur_min = min(candidates)
            result = max(result, cur_max)
        
        return result
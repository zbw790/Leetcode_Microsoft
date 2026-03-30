class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        current_sum = 0
        for i in range(len(nums)):
            current_sum += nums[i]
            nums[i] = current_sum

        return nums

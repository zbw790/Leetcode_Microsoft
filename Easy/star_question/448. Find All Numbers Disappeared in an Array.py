class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # temp_arr = [0] * len(nums)
        # for num in nums:
        #     if temp_arr[num - 1] == 0:
        #         temp_arr[num - 1] += 1
        
        # result = []
        # for i in range(len(temp_arr)):
        #     if temp_arr[i] == 0:
        #         result.append(i + 1)
        
        # return result
        for num in nums:
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] = nums[abs(num) - 1] * -1
        
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result
        
        #利用负号下标数组节省空间
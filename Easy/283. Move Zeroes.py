class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        first_pointer = self.get_initial_i(nums)
        second_pointer = first_pointer + 1
        if len(nums) > 1 and first_pointer != -1:
            while second_pointer != len(nums):
                if nums[second_pointer] != nums[first_pointer]:
                    nums[first_pointer] = nums[second_pointer]
                    nums[second_pointer] = 0
                    first_pointer += 1
                    second_pointer += 1
                else:
                    second_pointer += 1


        """
        Do not return anything, modify nums in-place instead.
        """

    def get_initial_i(self, nums):
        for i in range(len(nums)):
            if nums[i] == 0:
                return i
        return -1
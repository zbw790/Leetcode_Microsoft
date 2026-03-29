class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer1 = 0 #指向最初的几个独立element
        pointer2 = 1 #指向最新的element
        while pointer2 < len(nums):
            if nums[pointer1] == nums[pointer2]:
                pointer2 += 1
            else:
                pointer1 += 1
                nums[pointer1] = nums[pointer2]
                pointer2 += 1
        
        return pointer1 + 1

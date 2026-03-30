class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_map = {}
        monotonic_stack = []

        for num in nums2:
            while monotonic_stack != [] and num > monotonic_stack[-1]:
                smaller_num = monotonic_stack.pop()
                num_map[smaller_num] = num
            monotonic_stack.append(num)
        
        for i in range(len(nums1)):
            if nums1[i] in num_map:
                nums1[i] = num_map[nums1[i]]
            else:
                nums1[i] = -1
        
        return nums1

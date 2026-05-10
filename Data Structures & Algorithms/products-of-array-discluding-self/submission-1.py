class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # prefix arr 
        # suffix arr
        # Each index's number has 2 arr

        #           1 2 4 6
        # pre       1 2 8 48
        # post          24  6
        # output   48 24 12 8
        res = [1] * (len(nums))
        prefix, postfix = 1, 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(len(nums) -1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res

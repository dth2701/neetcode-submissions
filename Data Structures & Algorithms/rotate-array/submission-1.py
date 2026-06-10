class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        def reverse(l: int, r: int) -> None:
            while l < r: 
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        l, r = 0, len(nums) - 1
        reverse(l, r)
        reverse(l, k-1)
        reverse(k, r)
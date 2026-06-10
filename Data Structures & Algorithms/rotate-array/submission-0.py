class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Iterate each number with i-th index
        # Rotate from 0th to (k-1)-th number
        # For example: 0th index will swap with (k + i)-th index.
        # Time complexity: O(n)
        # Space complexity: O(1)
        n = len(nums)
        nums[:] = nums[n-k:] + nums[0:n-k]
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # 1. Count the frequency of each number with a dictionary.
        # Key: number and Value: its frequency
        # 2. Overwrite the current list of nums with the total number of 0's, then 1's and followed by 2's.
        # I will put those values back into nums start from (i+value)th index.
        # with i as the starting position for each number

        # Time complexity: O(n)
        # Space complexity: O(n)

        count = {}

        for num in nums: 
            count[num] = 1 + count.get(num, 0)
        
        i = 0
        for num in range(3):
            ending = int(i + count.get(num))
            while i < len(nums) and i < ending:
                nums[i] = num
                i += 1

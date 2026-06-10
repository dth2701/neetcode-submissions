class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Having the counter
        # 1. Iterate each num 
        # 2. Count if that number not a val
        #  a. Replace that number at position k
        #  b.
        # 3. Return the count

        # time complexity: O(n)

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

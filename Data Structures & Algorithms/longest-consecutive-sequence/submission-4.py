class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Identify the start of a sequence
        #   Using Set(no duplication) 
        #  a.  Start: check if the value of the current number - 1 exit 
        #       (not in set)  

        # 2. Keep track the max_length
        # Time complexity: O(n)
        i, max_len = 0, 0
        hashset = set(nums)

        while i < len(nums):
            count = 1
            if nums[i]-1 not in hashset:
                next_num = nums[i] + 1
                while next_num in hashset:
                    count += 1
                    next_num += 1
            if count > max_len:
                max_len = count
            i += 1

        return max_len

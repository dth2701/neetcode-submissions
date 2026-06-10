class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Identify the start of a sequence
        #   Using Set(no duplication) 
        #  a.  Start: check if the value of the current number - 1 exit 
        #       (not in set)  

        # 2. Keep track the max_length
        # Time complexity: O(n)

        hashset = set(nums)
        print(hashset)



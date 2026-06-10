class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1. Using dictionary to count the frequency of each number.
        # 2. Return the number with the max frequency
        hashmap = {}
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num, 0)
        return max(hashmap, key = hashmap.get)
            

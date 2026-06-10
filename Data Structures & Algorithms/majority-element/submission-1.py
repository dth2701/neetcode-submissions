class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 1. Using dictionary to count the frequency of each number.
        # 2. Return the number with the max frequency
        count = {}
        result = maxCount = 0
        for num in nums:
            count[num] = 1 + count.get(num, 0)
            if maxCount < count[num]:
                maxCount = count[num]
                result = num
        return result
            

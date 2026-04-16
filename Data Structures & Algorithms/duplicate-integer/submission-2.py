class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # new_nums = set(nums)
        # if len(new_nums) != len(nums): 
        #     return True
        # else:
        #     return False

        # check if a list having at least 1 num
        if len(nums) < 2: return False
        # having a dict that store key:num and value: counter
        dict = {}
        for num in nums:
            dict[num] = 1 + dict.get(num, 0)
        # Check if any value > 1, return true
        for num, count in dict.items():
            if count > 1: return True
        
        return False




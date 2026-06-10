class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, swap = 1,1

        while i < len(nums):
            if nums[i] != nums[swap-1]:
                temp = nums[i]
                nums[i]= nums[swap]
                nums[swap] = temp
                swap += 1
            
            i+=1
        return swap
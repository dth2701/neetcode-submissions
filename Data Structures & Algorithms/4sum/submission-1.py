class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i > 0:
                continue    

            for j in range(i+1,len(nums)):
                if nums[j] == nums[j-1] and j > i+1:
                    continue
                l, r = j+1, len(nums) - 1
                if l < r and nums[i] + nums[j] + nums[l] + nums[r] > target:
                    break

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total == target:
                        result.append([nums[i], nums[j],nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1

                    elif total > target:
                        r -= 1
                    else:
                        l += 1
        return result         

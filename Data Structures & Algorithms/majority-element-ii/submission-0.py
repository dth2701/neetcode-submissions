class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Having an result list
        # Create a dictionary to track each number and its frequencies.
        # if that key having the value is equal and more than n/3 and that key not in the result list yet, 
        # add that key on the result array
        # return the result list

        # time complexity: O(n) and n represent for the total numbers of nums
        # Space complexity: O(n)

        # Pick 2 candiates and counts its frequencies.

        count = {}
        result = set()
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)

            if count[num] > len(nums) // 3:
                result.add(num)
        return list(result)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # Having an result list
        # Create a dictionary to track each number and its frequencies.
        # if that key having the value is equal and more than n/3 and that key not in the result list yet, 
        # add that key on the result array
        # return the result list

        # time complexity: O(n) and n represent for the total numbers of nums
        # Space complexity: O(n)

        # count = {}
        # result = set()
        # checker = len(nums) // 3
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)

        #     if count[num] > checker:
        #         result.add(num)
        # return list(result)

        # Pick 2 candiates and counts its frequencies.
        # See a candidate, increase its count
        # Elif different, decrease its count
        # if the count is 0, replace the candidate.

        # Refresh: count the actual occurences of both candiate
        candidate1, candidate2 = -1,-1
        count1, count2 = 0, 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            
            else: 
                count1 -= 1
                count2 -= 1

        realCount1, realCount2 = 0, 0
        for num in nums:
            if num == candidate1:
                realCount1 += 1
            elif num == candidate2:
                realCount2 += 1

        n = len(nums)      
        result = []
        if realCount1 > n // 3: 
            result.append(candidate1)
        if realCount2 > n // 3: 
            result.append(candidate2)     

        return result  




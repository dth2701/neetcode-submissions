class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Create a hashmap with the first key-value pair is (0,1) because we assume the first num has its prefixSum as 0
        # For each number,
            # 1. Calculate the current prefixSum
            # 2. Calculate diff = prefixSum - k.
            # 3. if that diff is one of the key of HM(prev prefixSum), 
                # compute its count to the result.
            # 4. Then, Add that current prefixSum to the hashMap 
        # Return the result.
        # Time complexity: O(n) for lookup
        # Space complexity: O(n)

        hashmap = {}
        hashmap[0] = 1
        prefixSum, result = 0, 0
        for num in nums:
            prefixSum += num
            diff = prefixSum - k
            if diff in hashmap:
                result += hashmap.get(diff)
            hashmap[prefixSum] = 1 + hashmap.get(prefixSum, 0)
        return result
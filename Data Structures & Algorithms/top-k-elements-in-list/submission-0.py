class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1 1 1 2 2 3 100     k = 2
        # 1: 3
        # 2: 2
        # 3: 1
        # 100: 1

        counter = {}
        for num in nums:
            counter[num]= 1 + counter.get(num, 0)
        
        buckets = [[] for i in range(len(nums)+1)]
        # 0 ->
        # 1 -> [100]
        # 2 -> [2]
        # 3 -> [1]
        for num, freq in counter.items():
            buckets[freq].append(num)

        result = []
        for i in range(len(buckets) -1, 0, -1):
            for n in buckets[i]:
                result.append(n)
                if len(result) == k: 
                    return result







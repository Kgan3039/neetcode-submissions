class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        res = []

        for n in nums:
            if n not in freq:
                freq[n] = 0

            freq[n] += 1
        
        bucket = [[] for i in range (len(nums) + 1)]

        for n, count in freq.items():
            bucket[count].append(n)

        for count in range(len(bucket) - 1, 0, -1):
            for n in bucket[count]:
                res.append(n)
            
            if len(res) == k:
                return res


        

        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        buckets = [[] for i in range(len(nums) + 1)]

        for number, count in freq.items():
            buckets[count].append(number)


        result = []
        for i in range(len(nums), 0, -1):
            for numbers in buckets[i]:
                result.append(numbers)

                if len(result) == k:
                    return result









        

            
            
        



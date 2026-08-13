class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        
        for i, n in enumerate(nums):
            summand = target - n

            if summand not in seen:
                seen[n] = i
            else:
                return [seen[summand], i]
                
            
        
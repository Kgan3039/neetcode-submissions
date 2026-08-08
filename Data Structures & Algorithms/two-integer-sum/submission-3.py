class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
      checked = {}


      for i, n in enumerate(nums):
        summand = target - n
        if summand not in checked:
            checked[n] = i
        else:
            return [checked[summand], i]




          
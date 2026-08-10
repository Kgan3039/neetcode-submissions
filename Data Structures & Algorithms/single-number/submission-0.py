class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        check = {}

        for n in nums:
            check[n] = check.get(n, 0) + 1


        for output in check.keys():
            if check[output] == 1:
                return output
        
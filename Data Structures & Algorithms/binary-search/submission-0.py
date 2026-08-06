class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) <= 0:
            return -1
        
        l = 0
        r = len(nums) - 1
       
        while l <= r:
            m = (r+l)//2

            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1

            if (nums[m] == target):
                return m
        
        return -1

            

            

        
        
            
        

    


        
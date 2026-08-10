class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) == 0:
            return 0
        
        left = 0
        right = 1
        output = 1
        seen = set()
        seen.add(s[left])

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                right += 1
                tempOutput = (right - left)
                output = max(output, tempOutput)
            else:
                seen.discard(s[left])
                left += 1


        return output
            
            


            

        
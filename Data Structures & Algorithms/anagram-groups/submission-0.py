class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        freq = {}
        
        for s in strs:
            count = [0] * 26
        
            for char in s:
                count[ord(char) - ord("a")] += 1

            key = tuple(count)

            if key not in freq:
                freq[key] = []
            freq[key].append(s)
        
        return list(freq.values())



            


        
            




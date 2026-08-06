class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sMap = {}
        tMap = {}

        for charS in s:
            sMap[charS] = sMap.get(charS, 0) + 1
            
        for charT in t:
            tMap[charT] = tMap.get(charT, 0) + 1

        return sMap == tMap


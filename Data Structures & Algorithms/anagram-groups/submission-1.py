class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seenCombo = {}
        
        for s in strs:
            checklist = [0] * 26
            for char in s:
                checklist[ord(char) - ord("a")] += 1

            update = tuple(checklist)

            if update not in seenCombo:
                seenCombo[update] = []

            seenCombo[update].append(s)

        return list(seenCombo.values())
                

        



            

        

            
            

        
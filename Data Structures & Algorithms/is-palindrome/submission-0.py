class Solution:
    def isPalindrome(self, s: str) -> bool:

        characters = []

        for char in s:
            if char.isalnum():
                characters.append(char.lower())

        i = 0
        j = len(characters) - 1

        while i < j:
            if characters[i] == characters[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
            

        
            



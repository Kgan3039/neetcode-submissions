class Solution:
    def isPalindrome(self, s: str) -> bool:
        myList = []

        for char in s:
            if char.isalnum():
                myList.append(char.lower())
        
        
        i = 0
        j = len(myList) - 1

        while i <= j:
            if myList[i] != myList[j]:
                return False
            else:
                i += 1
                j -= 1

        return True
            

        
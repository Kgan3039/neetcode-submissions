class Solution:
    def isValid(self, s: str) -> bool:

        storage = []


        for char in s:
            if char == "{" or char == "(" or char == "[":
                storage.append(char)

            elif char == "}":
                if len(storage) == 0 or storage[-1] != "{":
                    return False
                storage.pop()

            elif char == ")":
                if len(storage) == 0 or storage[-1] != "(":
                    return False
                storage.pop()

            elif char == "]":
                if len(storage) == 0 or storage[-1] != "[":
                    return False
                storage.pop()
        
        return len(storage) == 0
        
                    
                


        
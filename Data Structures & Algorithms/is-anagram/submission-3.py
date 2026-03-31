class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if (len(s) != len(t)):
            return False
        
        count = {}

        for char in s:
            if char not in count:
                count[char] = 1
            else:
                count[char] += 1

        for char in t:
            if char not in count:
                return False
            else:
                count[char] -= 1
        
        for key in count:
            if count[key] != 0:
                return False
    
        return True


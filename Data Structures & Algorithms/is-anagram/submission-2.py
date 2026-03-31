class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1 = {}
        word2 = {}
        
        for char in s:
            if char not in word1:
                word1[char] = 1
            else:
                word1[char] +=1
        
        for char in t:
            if char not in word2:
                word2[char] = 1
            else:
                word2[char] +=1

        return (word1 == word2)
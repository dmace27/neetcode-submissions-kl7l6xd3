class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = 0
        k = len(s) - 1
        
        for i in range(len(s)):
            if j > k:
                break
            
            if not s[k].isalnum():
                k -= 1
            elif not s[j].isalnum():
                j += 1
            else:
                if s[j].lower() != s[k].lower():
                    return False
                j += 1
                k -= 1
        return True
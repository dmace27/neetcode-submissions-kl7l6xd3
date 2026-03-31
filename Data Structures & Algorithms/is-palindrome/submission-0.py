class Solution:
    def isPalindrome(self, s: str) -> bool:
        j, k = 0, len(s) - 1

        while j < k:
            if not s[j].isalnum():
                j += 1
            elif not s[k].isalnum():
                k -= 1
            else:
                if s[j].lower() != s[k].lower():
                    return False
                j += 1
                k -= 1

        return True
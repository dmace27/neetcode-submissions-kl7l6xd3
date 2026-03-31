class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        length = 1
        n = len(s)
        d = {}
        r = 0
        l = 0
        m = 0
        maxf = 0
        if n == 0:
            return n
        # sliding window
        while r < n:
            if s[r] in d:
                d[s[r]] += 1
            else:
                d[s[r]] = 1
            
            maxf = max(maxf, d[s[r]])
            
            
            # if the window passes the condition -> extend window
            # if k + the frequency of the most popular letter in the window is 
            # greater than or equal to the size of the window -> the window passes
            if r - l + 1 - maxf <= k:
                # only checks for a new longest window if the current window is valid
                
                if r - l + 1 > length:
                    length = r - l + 1
            
                

            # if the window fails the condition -> retract window
            else:
                d[s[l]] -= 1
                l += 1
            r += 1
        return length
            

            
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 1 # the substring is at least 1 long (provided the string length is not 0)
        n = len(s)
        d = {} 
        i = 0 
        j = 1
        # if there are less than 2 characters, there cannot be repeating characters 
        if n < 2:
            return n
        else:
            # setting up the initial window
            d[s[0]] = 1
            # in the case the first two chars are the same
            if s[1] in d:
                d[s[1]] += 1
            else:
                d[s[1]] = 1
        # loop should end when reaches n - 1 and runs once 
        # because after that the window can only get smaller
        while j+1 < n:
            # if there are no current duplicates, extend
            if len(d) == j - i + 1:
                j += 1
                if s[j] in d:
                    d[s[j]] += 1
                else:
                    d[s[j]] = 1
            # if there are current duplicates, retract
            else:
                d[s[i]] -= 1
                if d[s[i]] <= 0:
                    del d[s[i]]
                i += 1           
            # if length is bigger than it ever has been
            if len(d) > l:
                l = len(d)    
        
        # should run once if the while loop never runs
        if len(d) > l:
            l = len(d)

        return l
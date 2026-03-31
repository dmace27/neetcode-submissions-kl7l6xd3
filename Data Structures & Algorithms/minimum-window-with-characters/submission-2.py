class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ns = len(s)
        nt = len(t)
        ds = {}
        dt = {}
        # initial freq maps for both strings
        for i in range(nt):
            if t[i] not in dt:
                dt[t[i]] = 1
            else:
                dt[t[i]] += 1
        for i in range(ns):
            if s[i] not in ds:
                ds[s[i]] = 1
            else:
                ds[s[i]] += 1
        # there are more unique letters in t than in s
        if len(dt) > len(ds) or len(t) > len(s):
            return ""
        
        solution_found = False
        rmin = 0
        lmin = 0
        minw = 1001
        l = 0
        # current window
        w = {}
        matches = 0
        for r in range(ns):
            # adding the next letter to the map
            if s[r] not in w:
                w[s[r]] = 1
            else:
                w[s[r]] += 1
            
            # check if the new character meets its match
            if s[r] in dt and w[s[r]] == dt[s[r]]:
                matches += 1
            
            while matches == len(dt):
                if minw > r - l + 1:
                    solution_found = True
                    minw = r - l + 1
                    rmin = r
                    lmin = l 
                # if the matches are about to be broken
                if s[l] in dt and w[s[l]] == dt[s[l]]:   
                    matches -= 1              
                
                w[s[l]] -= 1
                l += 1
                

        if not solution_found:
            return ""
        return s[lmin:rmin + 1]












class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        w = len(s1)
        n = len(s2)
        d = {}
        map1 = {}
        l = 0
        r = w - 1
        matches = 0
        if w > n:
            return False
        # setting up initial freq maps for window and s1
        for i in range(w):
            if s2[i] not in d:
                d[s2[i]] = 1
            else:
                d[s2[i]] += 1

            if s1[i] not in map1:
                map1[s1[i]] = 1
            else:
                map1[s1[i]] += 1

        # count initial matches
        for key in map1:
            if key in d and d[key] == map1[key]:
                matches += 1
        if matches == len(map1):
                return True

        # fixed size sliding window
        for i in range(w, n):
            # incrementing the window
            # expand right side
            r += 1
            if s2[r] in map1 and s2[r] in d and d[s2[r]] == map1[s2[r]]:
                matches -= 1

            # adding the character to the dict
            if s2[r] not in d:
                d[s2[r]] = 1
            else:
                d[s2[r]] += 1
            
            # check for new matches
            if s2[r] in map1 and d[s2[r]] == map1[s2[r]]:
                matches += 1
            
            # if there is a current match, decrement 
            # s2[l] will get decremented in the next step
            if s2[l] in map1 and d[s2[l]] == map1[s2[l]]:
                matches -= 1

            # expand the left side
            d[s2[l]] -= 1

            if s2[l] in map1 and d[s2[l]] == map1[s2[l]]:
                matches += 1

            # increment l
            l += 1
            
            if matches == len(map1):
                return True

        return False

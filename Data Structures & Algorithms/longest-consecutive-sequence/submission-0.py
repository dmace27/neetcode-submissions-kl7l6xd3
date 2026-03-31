class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        fre = set()
        seq = {}
        longest = 0
        for i in nums:
            if i not in fre:
                fre.add(i)
        
        for i in fre:
            # if i-1 is not in the set it is the start of a sequence
            if (i-1) not in fre:
                j = i
                # loop through the set until the next consecutive number isnt there
                while (j+1) in fre:
                    j += 1
                # add the start and end of the sequence to a hashmap
                seq[i] = j + 1
        
        # loop over all the sequences
        for i in seq:
            length = seq[i] - i
            if length > longest:
                longest = length

        return longest
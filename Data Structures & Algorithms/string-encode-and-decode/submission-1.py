class Solution:

    def encode(self, strs: List[str]) -> str:
        n = len(strs)
        s = ""
        # adding original number of n strings to the start of the string
        if n > 99:
            s = s + str(n)
        elif n > 9:
            s = s + "0" + str(n)
        else:
            s = s + "00" + str(n)
        
        # adding the lengths of all the strings to the string
        for i in range(n):
            l = len(strs[i])
            if l > 99:
                s = s + str(l)
            elif l > 9:
                s = s + "0" + str(l)
            else:
                s = s + "00" + str(l)
        
        # adding the elements of strs to the string
        for i in strs:
            s += i
        return s


    def decode(self, s: str) -> List[str]:
        n = int(s[0:3])
        l = []
        ans = []
        # putting lengths of all the strings into the array
        for i in range(n):
            start = (i + 1) * 3
            end = start + 3
            l.append(int(s[start:end]))
        
        count = (n + 1) * 3
        for i in range(n):
            start = count
            end = count + l[i]

            ans.append(s[start:end])
            count += l[i]

        return ans 



















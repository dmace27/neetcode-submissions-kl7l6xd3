class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        seen_words = {}
        for i in range(len(strs)):
            letter_list = [0] * 26
            for ch in range(len(strs[i])):
                letter_list[ord(strs[i][ch]) - ord("a")] += 1

            key = tuple(letter_list)

            if key not in seen_words:
                seen_words[key] = []

            seen_words[key].append(strs[i])

        return list(seen_words.values())
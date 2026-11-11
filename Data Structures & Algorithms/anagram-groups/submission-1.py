from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # initialize dict 
        anagram_dict = defaultdict(list)

        for w in strs:
            count = [0] * 26

            for l in w:
                count[ord(l) - ord("a")] += 1

            anagram_dict[tuple(count)].append(w)
        return list(anagram_dict.values())


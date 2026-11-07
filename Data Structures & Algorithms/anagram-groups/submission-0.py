from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list) # map char count to list of anagrams

        for s in strs: #for each word in strs
            count = [0] * 26 # from a-z

            for c in s: #for each char in each word in strs
                count[ord(c) - ord("a")] += 1 # ord gives ascii val
            
            key = tuple(count)
            anagram_dict[key].append(s)

        return list(anagram_dict.values())


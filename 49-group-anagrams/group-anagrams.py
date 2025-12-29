class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        
        anagrams = defaultdict(list)

        for s in strs:
            freq = [0] * 26

            for ch in s:
                freq[ord(ch) - ord("a")] += 1
                

            key = tuple(freq)
            anagrams[key].append(s)

        return list(anagrams.values())
        

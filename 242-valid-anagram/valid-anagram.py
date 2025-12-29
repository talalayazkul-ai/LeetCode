class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freqs = {}
        freqt = {}
        if len(s) != len(t):
            return False

        for ch in s:
            freqs[ch] = freqs.get(ch, 0) + 1

        for ch in t:
            freqt[ch] = freqt.get(ch, 0) + 1

        return freqs == freqt
         


        
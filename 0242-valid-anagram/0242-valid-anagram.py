class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq:
                freq[s[i]] = 1
            else:
                freq[s[i]] += 1
        print(freq)
        
        
        for i in range(len(t)):
            if t[i] in freq:
                if freq[t[i]] > 0:
                    freq[t[i]] -= 1
            else:
                freq[t[i]] = 1
        
        count = 0
        for v in freq.values():
            count += v
        return True if count == 0 else False
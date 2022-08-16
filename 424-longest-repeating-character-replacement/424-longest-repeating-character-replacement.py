class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = {}
        res = 0 
        l = 0
        r = 0
        maxFreq = 0
        while r < len(s):
            count[s[r]] = 1 + count.get(s[r],0)
            maxFreq = max(maxFreq, count[s[r]])
            
            if (r-l+1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r-l + 1)
            r += 1
            
        return res
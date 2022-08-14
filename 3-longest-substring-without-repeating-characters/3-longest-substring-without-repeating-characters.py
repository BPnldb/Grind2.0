class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int

        """
        #Time Complexity : O(N)
        #Space Complexity : O(N)
        

        charSet = set()
        left = 0
        right = 0
        res = 0
        
        while right < len(s):
            while s[right] in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(s[right])
            res = max(res, right - left + 1)
            right += 1
        return res
            
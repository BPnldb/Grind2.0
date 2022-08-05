class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freq = {}
        
        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        for i in t:
            if i in freq:
                if freq[i] > 0:
                    freq[i] -= 1
            else:
                freq[i] = 1
        print(freq)
        count = 0
        for i in freq.values():
            count += i
        if count == 0:
            return True
        else:
            return False
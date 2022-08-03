class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        
        #Time Complexity : O(N) = 2N
        # Spaec Complexity: O(n)
        dic = {}
        
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 1
            else:
                dic[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in dic:
                dic[t[i]] = 1
            else:
                if dic[t[i]] > 0:
                    dic[t[i]] -= 1
        
        count = 0
        for i in dic.values():
            count += i
        return True if count == 0 else False
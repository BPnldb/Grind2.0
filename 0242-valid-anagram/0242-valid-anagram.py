class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashMap = {}
        for i in range(len(s)):
            if s[i] not in hashMap:
                
                hashMap[s[i]] = 1
            else:
                hashMap[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] in hashMap:
                if hashMap[t[i]] > 0:
                    hashMap[t[i]] -= 1
            else:
                hashMap[t[i]] = 1
            
        if sum(hashMap.values()) == 0:
            return True
        else:
            return False
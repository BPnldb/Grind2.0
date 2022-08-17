class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        
        -lowercase letters
        brute force:
            -sliding window
            -compare window of s1 within s2
            -CANT SORT
            
        - use hash(O(N)
        - keep track of counting the characters
        
        -compare s1dic and s2dic to eachother
            -if s1 is in s2
                - then return true
                
        """
        s1Count = {}
        s2Count = {}
        
        if len(s1) > len(s2):
            return False
        for i in range(len(s1)):
            s1Count[s1[i]] = 1 + s1Count.get(s1[i],0)
            s2Count[s2[i]] = 1 + s2Count.get(s2[i],0)
        
        
        if s1Count == s2Count:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            s2Count[s2[right]] = 1 + s2Count.get(s2[right],0) 
            
            s2Count[s2[left]] -= 1 #delete the left most
            
            
            if s2Count[s2[left]] == 0:
                s2Count.pop(s2[left])
            left += 1
            if s1Count == s2Count:
                return True
            
        return False
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
        

                
        
                
        charFreq = {} # Keep track of all characters in s1 and their frequency
        for char in s1:
            if char not in charFreq:
                charFreq[char] = 0
            charFreq[char] += 1
        
        matched = 0 # Keep track of how many characters in charFreq we have completely found
        windowStart = 0
        
        for windowEnd in range(len(s2)):
            char = s2[windowEnd] # Current character we are on
            
            if char in charFreq:
                charFreq[char] -= 1
                # If we found all instances of this character
                if charFreq[char] == 0:
                    matched += 1 # Increment matched by 1 since we have matched this character
            
            # If our window size exceeds the size of s1 we need to shrink our window
            while (windowEnd - windowStart + 1) > len(s1):
                remove = s2[windowStart]
                
                if remove in charFreq:
                    # We are removing this character from our window
                    # If we reach the point where we are adding characters back into charFreq
                    # then we must decrement matched since we no longer are matching that character fully
                    if charFreq[remove] == 0:
                        matched -= 1
                    charFreq[remove] += 1
                windowStart += 1
            
            # If the matched count is equal to the total number of characters in charFreq
            # then we have matched every character, hence we found a permutation
            if matched == len(charFreq):
                return True
        return False
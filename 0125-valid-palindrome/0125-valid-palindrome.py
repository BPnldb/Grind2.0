class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = s.lower()
        
        left, right = 0, len(newS) - 1

        while left < right:
            while left< right and not newS[left].isalnum():
                left += 1
            while left<right and not newS[right].isalnum():
                right -= 1
            if newS[left] == newS[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
        
                    
                    
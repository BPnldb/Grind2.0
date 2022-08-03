class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        
        Time Complexity : O(N * LogN) for N is length of string and LogN is sorting each char in the string
        Space COmplexity : O(N)
        """
    
        dic = {}
        
        for i in strs:
            sortedStrings = "".join(sorted(i))
            if sortedStrings not in dic:
                dic[sortedStrings] = [i]
            else:
                dic[sortedStrings].append(i)
        result = []
        
        for i in dic.values():
            result.append(i)
            
        return result
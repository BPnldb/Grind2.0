class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # only add open ( if open < n
        #only add closing ) if closed < open
        #valid IIF open == closed == n
        
        
        stack , res = [],[]
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                
            if openN < n:
                stack.append("(")
                backtrack(openN +1 , closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN,closedN+1)
                stack.pop()
        
        
        backtrack(0,0)
        
        return res
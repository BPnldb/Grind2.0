class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # only add open ( if open < n
        #only add closing ) if closed < open
        #valid IIF open == closed == n
        
        
        stack = []
        res = []
        
        
        self.backtrack(0,0,n,stack,res)
        return res
    def backtrack(self, openN, closedN,n,stack,res):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                self.backtrack(openN + 1, closedN,n,stack,res)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                self.backtrack(openN,closedN + 1,n,stack,res)
                stack.pop()
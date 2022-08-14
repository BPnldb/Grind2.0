class Solution(object):
    def isValid(self, s):
        
        
        #Time Complexity : O(N) for size of s
        #Space Complexity: O(N) for extra stack space
        # stack = []
        # for i in s: 
        #     if len(stack) == 0: 
        #         stack.append(i)
        #     elif stack[-1] == '{' and i == '}':
        #         stack.pop()
        #     elif stack[-1] == '(' and i == ')':
        #         stack.pop()
        #     elif stack[-1] == '[' and i == ']':
        #         stack.pop()
        #     else: 
        #         stack.append(i)
        # return False if stack else True
        
        
        stack = [] 
        dic = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        
        for i in range(len(s)):
            if s[i] in dic:
                #do
                if stack and stack[-1] == dic[s[i]]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        return True if len(stack) == 0 else False
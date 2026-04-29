class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack=[]
        
        for char in s:
            if char=='[' or char=='{' or char=='(':
                stack.append(char)
                
            else:
                if not stack: return False
                
                if(char=='}' and stack[-1]=='{') or (char==')' and stack[-1]=='(') or (char==']' and stack[-1]=='['):
                    stack.pop()
                    continue
                else: return False
        return len(stack)==0

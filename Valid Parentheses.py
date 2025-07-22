class Solution(object):
    def isValid(self, s):
        stack=[]
        mapping= {")" : "(", "]":"[" , "}":"{"}
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping:
                if not stack or stack[-1] !=mapping[char]:
                    return False
                stack.pop()
            else:
                return False
        return not stack
       

        


        """
        :type s: str
        :rtype: bool
        """
        

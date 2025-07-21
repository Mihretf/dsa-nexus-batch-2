class Solution(object):
    def interpret(self, command):
        result=""
        i=0
        while i < len(command):
            if command[i] == "G":
                result += "G"
                i+=1
            elif i+1 <len(command) and command[i] == "(" and command[i+1] == ")":
                result += "o"
                i+=2
            elif i+3 <len(command) and command[i] == "(" and command[i+1] == "a" and command[i+2] == "l" and command[i+3] == ")":
                result += "al" 
                i+=4

        return result
        

        """
        :type command: str
        :rtype: str
        """
        

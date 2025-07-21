class Solution(object):
    def freqAlphabets(self, s):
        result=""
        i=0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                num_str= s[i]+s[i+1]
                num= int(num_str)
                char= chr(96+num)
                result+=char
                i+=3
            else:
                num_char= s[i]
                num= int(num_char)
                char= chr(96+num)
                result+=char
                i+=1
        return result

    """
        :type s: str
        :rtype: str
        """
        

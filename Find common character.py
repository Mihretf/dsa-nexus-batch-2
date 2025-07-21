class Solution(object):
    def commonChars(self, words):
        result= list(words[0])
        for word in words[1:]:
            temp=[]
            for char in result:

                if char in word:
                    temp.append(char)
                    word= word.replace(char, "", 1)
                
            result= temp
       
        return result

    """
        :type words: List[str]
        :rtype: List[str]
        """
        

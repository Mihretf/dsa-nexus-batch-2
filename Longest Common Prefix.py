class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        first_word= strs[0]
        first_word_length= len(first_word)

        for index in range(first_word_length):
            current_char = first_word[index]
            other_words = strs[1:]
            for word in other_words:
                 word_length = len(word)
                 if index >=word_length or word[index]!= current_char:
                   return first_word[:index]
        return first_word
        




    
    """
        :type strs: List[str]
        :rtype: str
        """
        

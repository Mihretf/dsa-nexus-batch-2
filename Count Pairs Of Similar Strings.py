class Solution(object):
    def similarPairs(self, words):
        result =0
        n= len(words)
        
        for i in range(n):
            for j in range(i+1,n):

                set1= set(words[i])
                set2= set(words[j])

                if set1== set2:
                    result+=1
        return result
       
        """
        :type words: List[str]
        :rtype: int
        """
        

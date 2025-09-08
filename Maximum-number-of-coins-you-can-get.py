class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        piles.sort()
        n=len(piles)//3
        index = len(piles) -2
        total=0

        for i in range (n):
            total+=piles[index]
            index-=2
        return total

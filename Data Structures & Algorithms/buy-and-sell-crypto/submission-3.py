class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        the index of the values represent a day of the week,
        the value of the index represents the value of the money that could be either bought or sold for
        '''
        result = 0
        for i in range(len(prices)): #first loop for left pointer
            buy = prices[i]
            for j in range(i+1, len(prices)): #second loop for right point
                sell = prices[j]
                result = max(result, sell-buy)
        return result
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #同一天，可以先卖了，接着再买吗？ 如果这样操作的话，手续费岂不是白白交了？
        # 或者是需要T+1才能到账，所以不能当天卖了， 再以同样价格当天买？

        #算了，还是按照能够当天卖了有买的操作吧？
        if not prices:
            return 0
        result=0
        for i in range(0,len(prices)-1):
            if prices[i+1]>prices[i]:
                result+=prices[i+1]-prices[i]
        return result
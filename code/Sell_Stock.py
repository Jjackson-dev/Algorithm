class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_price = -sys.maxsize
        min_price = sys.maxsize
        profit = [0]
        for point in prices:
            if point < min_price:
                min_price = point
                max_price = -sys.maxsize
                continue
            elif point > max_price:
                max_price = point
            
            if min_price==sys.maxsize or max_price==-sys.maxsize:
                profit.append(0)
            
            else : profit.append(max_price-min_price)

        return max(profit)

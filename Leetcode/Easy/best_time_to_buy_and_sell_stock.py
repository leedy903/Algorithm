'''
Leetcode URL: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Problem: Best Time to Buy and Sell Stock, 121
Level: Easy
'''
import sys
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy, sell = 10000, 0
        profit = 0
        # buy_bakcup, sell_backup = 0
        # print(prices, end="\n\n")
        # print("price\tbuy\tsell\tprofit")
        for price in prices:
            if price <= buy:
                # 2 1 5,  2 5 1 
                buy = price
                sell = 0
            if price >= sell:
                sell = price
            if profit < sell - buy:
                profit = sell - buy
            # print("{}\t{}\t{}\t{}".format(price, buy, sell, profit))
        return profit
    
    # 파이썬 알고리즘 인터뷰 sol1, Brute Force
    def maxProfit1(self, prices: list[int]) -> int:
        max_price = 0

        for i, price in enumerate(prices):
            for j in range(i, len(prices)):
                max_price = max(prices[j]- price, max_price)

        return max_price

    # 파이썬 알고리즘 인터뷰 sol2, Calculate the difference between lowest point and present point
    def maxProfit2(self, prices: list[int]) -> int:
        profit = 0
        min_price = sys.maxsize # min_price = 10000, the question's max price condition is 10^4

        # update the min and max value
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)

        return profit


sol = Solution()

# TEST
test_inputs =[
        # Output: 5
        [7,1,5,3,6,4],
        # Output: 0
        [7,6,4,3,1],
        # Output: 7
        [7,3,5,3,6,4,2,9,1]
        ]

for test_input in test_inputs:
    print(sol.maxProfit(test_input))


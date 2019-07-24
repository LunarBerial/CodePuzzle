# coding: utf-8

'''
leetcode : 121 https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

注意：在不使用list属性前提下，遍历是最快捷的方案。
'''
def bestTime(prices):
    if len(prices) == 0:
        return 0
    max_money = 0  # 记录当前时间卖出所能获得的最大利润
    min_price = prices[0]  # 记录当前时间点之前出现过的最低价格，用于计算当前时间卖出最多能获得的利润
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        if prices[i] - min_price > max_money:
            max_money = prices[i] - min_price
    return max_money

if __name__== "__main__":
    print(bestTime([7,1,5,3,6,4]))

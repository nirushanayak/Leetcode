# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPos = [0]*len(prices)
        maxPos[len(prices)-1]=prices[len(prices)-1]
        for i in range(len(prices)-2,-1,-1):
            maxPos[i]=max(maxPos[i+1],prices[i])
        Profit=0
        for i in range(len(prices)):
            Profit=max(Profit, maxPos[i]-prices[i])
        return Profit


## sliding window method, uses O(1) space
# intution is buy when low, sell when high
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       l,r=0,1 #left=buy, right=sell
       profit=0
       while(r<len(prices)):
            #profitable?
            if prices[l]<prices[r]:
                profit=max(profit, prices[r]-prices[l])
            else:
                l=r
            r+=1
       return profit
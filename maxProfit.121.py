def maxProfit(prices):
    left = 0
    right = 1
    mProfit = 0
    while right < len(prices):
        if prices[right] > prices[left]:
            pr = prices[right] - prices[left]
            mProfit = max(mProfit, pr)
        else:
            left = right
        right += 1
    return mProfit

print(maxProfit([7,1,5,3,6,4]))

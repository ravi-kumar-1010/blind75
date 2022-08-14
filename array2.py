#%%
import sys
def ok(prices):
    profit = 0
    for i in range(1,len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
            print(prices[i],prices[i-1])
    return profit
# %%
ok([7,1,5,3,6,4])
# %%
ok([1,2,3,4,5])
# %%
ok([7,6,5,4,3,2,1])

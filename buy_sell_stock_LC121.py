
prices = [7,6,4,3,1]
n = len(prices)
buy_stock = prices.index(min(prices))
#print(buy_stock)

max_value = 0
for i in range(buy_stock, n):
    #if prices[buy_stock-1] > prices[buy_stock]:
    if prices[i] > max_value:
        max_value = prices[i]
profit = max_value - prices[buy_stock] 
print(profit)
    
# #print(prices[buy_stock:])
# if buy_stock 
# sell_stock = max(prices[buy_stock:]) 
# print(sell_stock)
# profit = sell_stock - buy_stock
#print(profit)



#for i in range(buy_stock,len(prices)):
    #if prices[i]
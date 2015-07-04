# time = minutes - 930;
# solution 1: n log n

stock_prices_yesterday = [1, 4, 3, 0, 0, 14, -1, 1, 1, 1, 2, 4, 7, 9, 10, -2, 50]

max_profit = stock_prices_yesterday[1] - stock_prices_yesterday[0]
current_min_buy_price = stock_prices_yesterday[0]
for time_index, buy_price in enumerate(stock_prices_yesterday[:-1]):
    if current_min_buy_price > buy_price:
        current_min_buy_price = buy_price
    
    if buy_price < stock_prices_yesterday[time_index + 1]:
    	if max_profit < stock_prices_yesterday[time_index + 1] - current_min_buy_price:
            max_profit = stock_prices_yesterday[time_index + 1] - current_min_buy_price
        
print max_profit
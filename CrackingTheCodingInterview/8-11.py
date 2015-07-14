"""
Coins:

how to make change with different coin denominations
"""

def Make_Change(coin_list, change_dict, smallest_coin, n):
	dict_key = str((n , smallest_coin))
	ways = 0

	if dict_key in change_dict:
		print "using cache [%s]" % dict_key
		return change_dict[dict_key]

	if n == 0:
		change_dict[dict_key] = 1
		return 1
	else:
		for c in [coin for coin in coin_list if coin <= n]:
			if c >= smallest_coin:
				ways += Make_Change(coin_list, change_dict, c,n-c)

	change_dict[dict_key] = ways
	return ways

n = 4
coin_list = [1, 2, 3]
change_dict = {}
print Make_Change(coin_list, change_dict, min(coin_list), n)
print change_dict
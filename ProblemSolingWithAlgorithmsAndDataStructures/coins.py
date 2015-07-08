import locale
locale.setlocale(locale.LC_ALL, 'en_US')

def dynamic_coins(coin_list, change, run_count, known_results):
	run_count.num += 1
	print locale.format("%d", run_count.num, grouping=True)

	minCoins = change
	if change in coin_list:
		known_results[change] = 1
		return 1
	elif known_results[change] > 0:
		return known_results[change]
	else:
		for i in [c for c in coin_list if c <= change]:
			numCoins = 1 + dynamic_coins(coin_list, change - i, run_count, known_results)
			if numCoins < minCoins:
				minCoins = numCoins
				known_results[change] = minCoins

	return minCoins

class Run_Count(object):
	def __init__(self, num):
		self.num = num
		
iter_count = Run_Count(0)
print dynamic_coins([1, 5, 10, 25], 63, iter_count, [0]*64)


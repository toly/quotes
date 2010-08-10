# -*- coding: utf-8

import quotes.quotes as quotes
import matplotlib.pyplot as plt

folder = 'data/'
qlist = 'quotes/mmvb.txt'
interval = 8

symbols = quotes.get_symbols(qlist)

# массив для хранения среднесуточных объемов торговли
volumes = []
# проходимся по всем акциям
for symb in symbols:
	# для каждой загружаем ранее сохраненные котировки за прошлый год
	q = quotes.quote(interval, int(symb[0]) )
	q.load( folder + str(symb[0]) + '_' + str(interval) + '.csv'  )
	# пробегаемся по всем дням текущей акции
	s = 0.0
	for i in xrange(len(q.volume)):
		# прибавляем торговый оборот за день
		s += q.volume[i] * (q.high[i] + q.low[i]) / 2.0
	# считаем среднее
	if len(q.volume) == 0:
		continue
	s = s / len(q.volume)
	# учет будем вести в миллионах
	s = s/1000000
	volumes.append(s)

# выводим гистограмму
plt.hist(volumes, 50)
plt.show()

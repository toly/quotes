# -*- coding: utf-8

import quotes.quotes as quotes

folder = 'data/'
qlist = 'quotes/mmvb.txt'
interval = 8

symbols = quotes.get_symbols(qlist)

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
	if s > 1500:
		print '\t', symb[0], '\t', symb[1]
		print '\tсреднесуточный оборот:', s, 'млн. рублей\n'

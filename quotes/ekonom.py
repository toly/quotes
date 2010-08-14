# -*- coding: utf-8
import quotes

# наследуем ранее созданный класс quote
class quote(quotes.quote):
	# moving average (скользящее среднее)
	def MA(self, period=7, price='c'):
		# массив для подготовки результатов
		res = []
		# выбор цены для рассчета
		if price == 'c':
			x = self.cl
		elif price == 'o':
			x = self.op
		elif price == 'h':
			x = self.hi
		elif price == 'l':
			x = self.lo
		else:
			x = []
		#  рассчитываем среднее
		for i in xrange(len(x)):
			if i < period:
				res.append(x[i])
			else:
				s = 0
				for j in range(i-period, i):
					s += x[j]
				res.append(s/period)
		return res

# экспоненциальное сглаживание
	def EMA(self, a=0.1, price='c'):
		# массив для подготовки результатов
		res = []
		# выбор цены для рассчета
		if price == 'c':
			x = self.cl
		elif price == 'o':
			x = self.op
		elif price == 'h':
			x = self.hi
		elif price == 'l':
			x = self.lo
		else:
			x = []
		#  рассчитываем экспоненциальные сглаживающие
		for i in xrange(len(x)):
			if i == 0:
                		res.append(x[i])
            		else:
                		ema = a * x[i] + (1.0 - a) * res[-1]
                		res.append(ema)
        	return res

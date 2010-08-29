# -*- coding: utf-8
import quotes

# расчет прогнозных значений методом Хольта
# на вход подается массив, на выходе - массив(несмещенный)
def halt(x, a, b, t=1.):
	y, y1, y2 = [], [], []
	for i in xrange(len(x)):
		if i == 0:
			y.append(x[i])
			y1.append(0.)
			y2.append(0.)
			continue
		if i == 1:
			y.append(x[i])
			y1.append(x[i])
			y2.append(x[i]-x[i-1])
			continue
		y1.append( a*x[i-1] + (1. - a)*(y1[-1] - y2[-1]) )
		y2.append( b*(y1[-1] -y1[-2]) + (1. - b)*y2[-1]  )
		y.append(y1[-1] + y2[-1]*t)
	return y

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
                		ema = a * x[i-1] + (1.0 - a) * res[-1]
                		res.append(ema)
        	return res

	def halt(self, a, b, t=1., price='c'):
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
		return halt(x, a, b, t)

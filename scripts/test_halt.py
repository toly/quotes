# -*- coding: utf-8

# подгружаем библиотеки
from quotes.ekonom import * 
import matplotlib.pyplot as plt

# начальные параметры
folder = 'data/'
qlist = 'quotes/mmvb.txt'
interval = 8

# финамовский номер газпрома
fnum = 16842

# загружаем котировки Газпрома из локальной базы
q = quote(interval,  fnum)
q.load(folder + str(q.symb) + '_' + str(interval) + '.csv')

# работать будем с ценами закрытия
x = q.cl
# по умолчания берутся цены закрытия
y = q.halt(.3, .2)
z = q.halt(.5, .2)


# как все было сложно если бы не ООП :)
'''
# задаем коэффициенты для первого прогноза
a, b = .5, .8
# формируем массивы тренда, микротренда и прогноза
y1, y2, y = [], [], []
for i in xrange(len(x)):
	if i == 0:
		y.append(x[i])
		y1.append(0.)
		y2.append(0.)
		continue
	if i == 1:
		y.append(x[i])
		y1.append(x[i])
		y2.append(x[i] - x[i-1])
		continue
	y1.append( a*x[i-1] + (1.-a)*( y1[-1] + y2[-1] ) )
	y2.append( b*(y1[-1] - y1[-2]) + (1.-b)*y2[-1] )
	y.append(y1[-1]+y2[-1])
# сохраняем прогноз
z = y

# формируем другой прогноз с другими коэффициентами
a, b = .4, .6
y1, y2, y = [], [], []
for i in xrange(len(x)):
	if i == 0:
		y.append(x[i])
		y1.append(0.)
		y2.append(0.)
		continue
	if i == 1:
		y.append(x[i])
		y1.append(x[i])
		y2.append(x[i] - x[i-1])
		continue
	y1.append( a*x[i-1] + (1.-a)*( y1[-1] + y2[-1] ) )
	y2.append( b*(y1[-1] - y1[-2]) + (1.-b)*y2[-1] )
	y.append(y1[-1]+y2[-1])
'''

# выводим на одном графике реальные значения и пронозы
plt.plot(x, label='real')
plt.plot(y, label='predict1')
plt.plot(z, label='predict2')
plt.legend()
plt.show()
